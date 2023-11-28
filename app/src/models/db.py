from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    func,
    NullPool,
)
from app.config import settings

if settings.MODE == "TEST":
    DB_URL = settings.test_database_url
    DB_PARAMS = {"poolclass": NullPool}
else:
    DB_URL = settings.database_url
    DB_PARAMS = {}

engine = create_async_engine(url=DB_URL, **DB_PARAMS)

async_session_maker = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


class BaseModel:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


Base = declarative_base(cls=BaseModel)
