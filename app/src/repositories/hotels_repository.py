from sqlalchemy import select

from app.src.api.exceptions import HotelNotFoundException
from app.src.models.db import async_session_maker
from app.src.models.hotels import Hotels
from app.src.repositories.base_repository import BaseRepository


class HotelsRepository(BaseRepository):
    model = Hotels

    async def get_by_location(self, location: str) -> list[Hotels]:
        async with async_session_maker() as session:
            query = select(Hotels).where(Hotels.location.contains(location))
            hotels = (await session.execute(query)).scalars().all()
            return hotels

    async def get_hotel_by_id(self, hotel_id: int) -> Hotels:
        hotel = await self.get_by_id(model_id=hotel_id)
        if not hotel:
            raise HotelNotFoundException
        return hotel


hotels_repository = HotelsRepository()
