from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    func,
)
from app.config import settings

engine = create_async_engine(url=settings.database_url)

async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class BaseModel:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


Base = declarative_base(cls=BaseModel)
