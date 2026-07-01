from fastapi import APIRouter
from fastapi import UploadFile
from app.services.file_service import FileService
router = APIRouter()
service = FileService()

@router.post("/upload")
async def upload(file: UploadFile):
    result = service.process(file)
    return result