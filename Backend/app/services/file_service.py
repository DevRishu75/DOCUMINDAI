from pathlib import Path
from fastapi import UploadFile
import shutil
import uuid

from app.ingestion.pdf_loader import PDFLoader
from app.ingestion.text_cleaner import TextCleaner
from app.chunking.chunker import Chunker
from app.services.embedding_service import EmbeddingService
from app.storage.vectorstore import VectorStore
# print(PDFLoader)
class FileService:# Blueprint for creating FileService objects
    """Handles all the files related to --
       Responsibilities
       Save uploaded files
       process pdf documents"""

    UPLOAD_FOLDER = Path("uploads") # class variable every FileService object shares it knows about 
    def __init__(self):   #method that a class can perform 
        self.UPLOAD_FOLDER.mkdir(exist_ok=True)

        self.pdf_loader = PDFLoader()   # Create a PDFLoader object and store it as an attribute
        # of this FileService instance.
        self.text_cleaner = TextCleaner()
        self.chunker = Chunker()
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()
    def save_uploaded_file(self, file:UploadFile) ->Path: #Method of an object means object can do this 

        file_path = self.UPLOAD_FOLDER/file.filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
        
        return file_path
    def process_pdf(self,file:UploadFile)->dict:
        #step 1: save file 
        saved_path = self.save_uploaded_file(file)
        print(f"Saved path : {saved_path}")
        #Extracted raw text
        raw_text = self.pdf_loader.extract_text(str(saved_path))
        #clean text 
        clean_text = self.text_cleaner.clean(raw_text)
        chunks = self.chunker.chunk(clean_text)
        print(type(chunks))
        print(chunks)
        print(f"chunks created : {len(chunks)}")
        embeddings = self.embedding_service.embed_chunks(chunks)
        print(f"embeddings generated : {len(embeddings)}")
        document_id = str(uuid.uuid4())
        ids = [
            f"{document_id}_chunk_{i}"
            for i in range(len(chunks))
        ]
        metadatas = [        #variables (attributes) a object(class) knows about 
            {
                "document_id":document_id,
                "source": file.filename,
                "chunk_index": i
            }
            for i in range(len(chunks)) 
        ]
        self.vector_store.add_document(ids,chunks,metadatas,embeddings)
        print("Stored vectors:", self.vector_store.collection.count())

        #step 4: Return Result
        return {
            "document_id": document_id,
            "filename": file.filename,
            "file_path": str(saved_path),
            "text_length": len(clean_text),
            "text_preview": clean_text[:1000],
            "message":"PDF processed successfully"
        }