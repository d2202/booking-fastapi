import asyncio
import json
from datetime import datetime
from typing import Any

import pytest
from httpx import AsyncClient
from sqlalchemy import insert

from app.src.models.db import Base, async_session_maker, engine
from app.config import settings

from app.src.models.bookings import Bookings
from app.src.models.hotels import Hotels
from app.src.models.rooms import Rooms
from app.src.models.users import Users
from app.src.main import app as fastapi_app


@pytest.fixture(scope="session", autouse=True)
async def prepare_db() -> None:
    assert settings.MODE == "TEST"
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(
            f"{settings.PATH_TO_MOCK}/mock_{model}.json", encoding="utf-8"
        ) as file:
            return json.load(file)

    hotels = open_mock_json("hotels")
    rooms = open_mock_json("rooms")
    users = open_mock_json("users")
    bookings = open_mock_json("bookings")

    for booking in bookings:
        booking["date_from"] = datetime.strptime(booking["date_from"], "%Y-%m-%d")
        booking["date_to"] = datetime.strptime(booking["date_to"], "%Y-%m-%d")

    async with async_session_maker() as session:
        add_hotels = insert(Hotels).values(hotels)
        add_rooms = insert(Rooms).values(rooms)
        add_users = insert(Users).values(users)
        add_bookings = insert(Bookings).values(bookings)

        await session.execute(add_hotels)
        await session.execute(add_rooms)
        await session.execute(add_users)
        await session.execute(add_bookings)

        await session.commit()


@pytest.fixture(scope="session")
def event_loop(request: Any) -> None:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def client() -> None:
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session")
async def authenticated_client() -> None:
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        await ac.post(
            url="/auth/login",
            json={
                # from mocked data, existing user
                "email": "test@test.com",
                "password": "test",
            },
        )
        assert ac.cookies["booking_access_token"]
        yield ac


@pytest.fixture(scope="function")
async def session() -> None:
    async with async_session_maker() as session:
        yield session
