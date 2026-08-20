from fastapi import APIRouter, UploadFile, File,Depends
from app.services.file_service import FileService
from sqlalchemy.orm import Session
from app.db.session import get_db

upload_router = APIRouter()

@upload_router.post('/api/v1/uploads')
async def Upload(file:UploadFile = File(...), 
                 db:Session = Depends(get_db)):
    service = FileService()
    return service.process_pdf(file,db)

 