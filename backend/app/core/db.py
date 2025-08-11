from sqlmodel import create_engine, SQLModel

from app.core.config import settings


engine = create_engine(str(settings.DATABASE_URI))

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)