from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.document_response import DocumentResponse
from app.services.document_service import DocumentService
from uuid import UUID

document_router = APIRouter()

@document_router.get('/api/v1/documents', response_model=list[DocumentResponse])
def get_documents(db: Session = Depends(get_db)):
    service = DocumentService()
    return service.get_documents(db)

@document_router.get('/api/v1/documents/{document_id}', response_model=DocumentResponse)
def get_document(document_id: UUID, db: Session = Depends(get_db)):
    service = DocumentService()
    document = service.get_document(document_id, db)
    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document Not Found"
        )
    return document

@document_router.delete('/api/v1/documents/{document_id}')
def delete_document(document_id: UUID, db: Session = Depends(get_db)):
    service = DocumentService()
    
    # Do NOT call get_document here. delete_document already handles existence check.
    result = service.delete_document(document_id, db)
    
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="No content found for this id"
        )
        
    return result