from fastapi import APIRouter
from fastapi import UploadFile
from app.services.file_service import FileService

router = APIRouter()

@router.post('api/v1/uploads')
async def Upload(file:UploadFile):
    service = FileService()
    return service.process_pdf()

