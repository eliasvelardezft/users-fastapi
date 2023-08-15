from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import SQLBaseModel
from config.settings import (
    DB_USER,
    DB_PASSWORD,
    DB_SERVER,
    DB_PORT,
    DB_NAME
)


DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}" 

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SQLBaseModel.metadata.create_all(bind=engine)
