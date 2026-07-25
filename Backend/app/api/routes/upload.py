from fastapi import APIRouter
from fastapi import UploadFile, File
from app.services.file_service import FileService

upload_router = APIRouter()

@upload_router.post('/api/v1/uploads')
async def Upload(file:UploadFile = File(...)):
    service = FileService()
    return service.process_pdf(file)

