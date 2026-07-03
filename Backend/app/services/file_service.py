from pathlib import Path
from fastapi import UploadFile
import shutil

from app.ingestion.pdf_loader import PDFLoader
from app.ingestion.text_cleaner import TextCleaner
print(PDFLoader)
class FileService:
    """Handles all the files related to --
       Responsibilities
       Save uploaded files
       process pdf documents"""

    UPLOAD_FOLDER = Path("uploads")
    def __init__(self):
        self.UPLOAD_FOLDER.mkdir(exist_ok=True)

        self.pdf_loader = PDFLoader()
        self.text_cleaner = TextCleaner()
    def save_uploaded_file(self, file:UploadFile) ->Path:

        file_path = self.UPLOAD_FOLDER/file.filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
        
        return file_path
    def process_pdf(self,file:UploadFile)->dict:
        #step 1: save file 
        saved_path = self.save_uploaded_file(file)

        #Extracted raw text
        raw_text = self.pdf_loader.extract_text(str(saved_path))
        #clean text 
        clean_text = self.text_cleaner.clean(raw_text)

        #step 4: Return Result
        return {
            "filename": file.filename,
            "file_path": str(saved_path),
            "text_length": len(clean_text),
            "text_preview": clean_text[:1000],
            "message":"PDF processed successfully"
        }