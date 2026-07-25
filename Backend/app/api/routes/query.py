from fastapi import APIRouter
from app.schemas.query_response import QueryRequest
from app.services.retrieval_service import RetrievalService
ask_router = APIRouter()

@ask_router.post('/api/v1/ask')
async def Ask_query(request:QueryRequest)->str:
    Retrieve = RetrievalService()
    Answer = Retrieve.retrieve(request.question)
    return Answer