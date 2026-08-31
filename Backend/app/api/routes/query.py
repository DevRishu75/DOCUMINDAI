from fastapi import APIRouter,Depends,HTTPException,status
from app.schemas.query_response import QueryRequest
from app.services.retrieval_service import RetrievalService
from app.models.user_model import User
from app.auth.dependecies import get_current_user
from uuid import UUID
from app.db.session import get_db
from sqlalchemy.orm import Session
ask_router = APIRouter()

@ask_router.post('/api/v1/ask/{document_id}')
async def ask_query(document_id:UUID,request:QueryRequest,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    retrieval_service = RetrievalService()
    retrieved_chunks = retrieval_service.retrieve(request.question,document_id,db,current_user)
    if retrieved_chunks is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document Not Found"
        )
    return retrieved_chunks