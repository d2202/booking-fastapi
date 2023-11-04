from app.src.models.bookings import Bookings
from app.src.repositories.base_repository import BaseRepository


class BookingRepository(BaseRepository):
    model = Bookings

    async def get_all_bookings(self) -> list[Bookings]:
        return await self.get_all()


booking_repository = BookingRepository()
