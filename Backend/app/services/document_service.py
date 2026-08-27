from pathlib import Path
from sqlalchemy.orm import Session
from app.models.document_model import Document
from app.storage.vectorstore import VectorStore
from app.services.file_service import FileService

class DocumentService:
    UPLOAD_FOLDER = Path('uploads')
    def __init__(self):
        self.vector_store = VectorStore()
    def get_documents(self,db:Session):
        documents =  db.query(Document).all()
        return [
            {
                "document_id": document.id,
                "filename": document.filename,
                "created_at": document.created_at
            }
            for document in documents
        ]
    def get_document(self,document_id,db:Session):
        document = db.query(Document).filter(Document.id==str(document_id)).first()
        if document is None:
            return None
        return {
            "document_id": document.id,
            "filename": document.filename,
            "created_at":document.created_at
        }
    def delete_document(self,document_id,db:Session):
        document = db.query(Document).filter(Document.id==str(document_id)).first()
        if document is None:
            return None
        file_path = self.UPLOAD_FOLDER/document.filename
        if file_path.exists():
            file_path.unlink()
        chunk_before_delete = self.vector_store.count_document_chunk(document_id)
        self.vector_store.delete_document(document_id)
        chunk_after_delete =  self.vector_store.count_document_chunk(document_id)
        db.delete(document)
        db.commit()
        return {
            "document_id":"...",
            "message": "Content deleted successfully"
        }