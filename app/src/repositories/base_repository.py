from typing import Self, Any

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.logger import logger
from app.src.models.db import async_session_maker

BASE_REPO_EXC_MSG = "Class attribute 'model' is None"


class BaseRepository:
    model = None

    @classmethod
    async def get_by_id(cls, model_id: int) -> Self:
        if cls.model is None:
            logger.error(msg=BASE_REPO_EXC_MSG)
            raise AttributeError(BASE_REPO_EXC_MSG)
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by: Any) -> Self:
        if cls.model is None:
            logger.error(msg=BASE_REPO_EXC_MSG)
            raise AttributeError(BASE_REPO_EXC_MSG)
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def get_by_filter(cls, **filter_by: Any) -> list[Self]:
        if cls.model is None:
            logger.error(msg=BASE_REPO_EXC_MSG)
            raise AttributeError(BASE_REPO_EXC_MSG)
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def get_all(cls) -> list[Self]:
        if cls.model is None:
            logger.error(msg=BASE_REPO_EXC_MSG)
            raise AttributeError(BASE_REPO_EXC_MSG)
        async with async_session_maker() as session:
            query = select(cls.model)
            return (await session.execute(query)).scalars().all()

    @classmethod
    async def add(cls, **data: Any) -> None:
        try:
            if cls.model is None:
                raise AttributeError(BASE_REPO_EXC_MSG)
            new_instance = cls.model(**data)

            async with async_session_maker() as session:
                session.add(new_instance)
                await session.commit()
        except SQLAlchemyError:
            logger.exception(
                msg=f"Database Exc: cannot add {cls.model}",
                extra={**data},
                exc_info=True,
            )
        except AttributeError:
            logger.exception(msg=BASE_REPO_EXC_MSG, exc_info=True)
