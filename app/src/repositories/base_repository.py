from typing import Self, Any

from sqlalchemy import select

from app.src.models.db import async_session_maker


class BaseRepository:
    model = None

    @classmethod
    async def get_by_id(cls, model_id: int) -> Self:
        if cls.model is None:
            raise AttributeError("Attribute 'model' is None")
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by: Any):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def get_by_filter(cls, **filter_by: Any):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def get_all(cls) -> Self:
        if cls.model is None:
            raise AttributeError("Attribute 'model' is None")
        async with async_session_maker() as session:
            query = select(cls.model)
            return (await session.execute(query)).scalars().all()

    @classmethod
    async def add(cls, **data: Any) -> None:
        if cls.model is None:
            raise AttributeError("Attribute 'model' is None")
        new_instance = cls.model(**data)
        async with async_session_maker() as session:
            session.add(new_instance)
            await session.commit()
