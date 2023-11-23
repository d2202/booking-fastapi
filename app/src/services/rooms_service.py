from app.src.models.rooms import Rooms
from app.src.repositories.rooms_repository import rooms_repository


class RoomsService:
    def __init__(self):
        self.repository = rooms_repository

    async def get_rooms_by_hotel_id(self, hotel_id: int) -> list[Rooms]:
        return await self.repository.get_by_filter(hotel_id=hotel_id)


rooms_service = RoomsService()
