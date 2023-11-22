from app.src.models.rooms import Rooms
from app.src.repositories.base_repository import BaseRepository


class RoomsRepository(BaseRepository):
    model = Rooms

    async def get_by_hotel_id(self, hotel_id: int) -> list[Rooms]:
        return await self.get_by_filter(hotel_id=hotel_id)


rooms_repository = RoomsRepository()
