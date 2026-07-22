from pydantic import BaseModel

class UploadResponse(BaseModel):
    filename :str
    filesize : str
    filetype: str
    message: str