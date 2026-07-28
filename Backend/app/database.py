from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
DATABASE = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE)
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind= engine
)
Base = declarative_base()
