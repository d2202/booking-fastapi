from app.src.models.bookings import Bookings
from app.src.repositories.base_repository import BaseRepository


class BookingRepository(BaseRepository):
    model = Bookings

    async def get_all_bookings(self) -> list[Bookings]:
        return await self.get_all()

    async def get_by_user_id(self, user_id: int) -> list[Bookings]:
        return await self.get_by_filter(user_id=user_id)


booking_repository = BookingRepository()
