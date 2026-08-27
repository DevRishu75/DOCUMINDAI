from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class DocumentResponse(BaseModel):
    document_id:UUID
    filename: str
    created_at:datetime
