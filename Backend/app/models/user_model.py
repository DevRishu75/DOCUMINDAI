from sqlalchemy import Column,String,DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db.base import Base
import uuid

class User(Base):
    __tablename__ = "users"

    user_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    email = Column(
        String(255), nullable=False, unique=True,index=True
    )
    password_hash = Column(
        String,nullable=False
    )
    created_at = Column(
        DateTime, nullable=False, default=datetime.utcnow
    )
