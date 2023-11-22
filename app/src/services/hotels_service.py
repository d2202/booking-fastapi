from datetime import date

from app.src.models.hotels import Hotels
from app.src.repositories.hotels_repository import hotels_repository


class HotelsService:
    def __init__(self):
        self.repository = hotels_repository

    async def get_hotels_by_location(
        self, location: str, date_from: date, date_to: date
    ) -> list[Hotels]:
        # TODO: add bookings filter date_from, date_to
        return await self.repository.get_by_location(location=location)

    async def get_hotel_by_id(self, hotel_id: int) -> Hotels:
        return await self.repository.get_hotel_by_id(hotel_id=hotel_id)


hotels_service = HotelsService()
