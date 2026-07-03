from pydantic import BaseModel

class uploadResponse(BaseModel):
    filename:str
    file_size:str
    file_type:str
    message:str