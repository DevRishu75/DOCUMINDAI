from pathlib import Path
from fastapi import UploadFile
import shutil

from app.ingestion.pdf_loader import PDFLoader
from app.ingestion.text_cleaner import TextCleaner
class File_service:
    """Handles all the files related to --
       Responsibilities
       Save uploaded files
       process pdf documents"""

    UPLOAD_FOLDER = Path("uploads")
    def __init__(self):
        self.UPLOAD_FOLDER.mkdir(exist_ok=True)

        self.pdf_loader = PDFLoader()
        self.text_cleaner = TextCleaner()
    def save_uploaded_file(self, file:UploadFile):

        file_path = self.UPLOAD_FOLDER/file.filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
        
        return file_path
