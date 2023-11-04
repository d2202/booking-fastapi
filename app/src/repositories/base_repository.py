from sqlalchemy import select

from app.src.models.db import async_session_maker


class BaseRepository:
    model = None

    @classmethod
    async def get_all(cls):
        if cls.model is None:
            raise AttributeError("Attribute 'model' is None")
        async with async_session_maker() as session:
            query = select(cls.model)
            return (await session.execute(query)).scalars().all()
