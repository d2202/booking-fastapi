from app.src.models.bookings import Bookings
from app.src.repositories.booking_repository import booking_repository


class BookingService:
    def __init__(self):
        self.repository = booking_repository

    async def get_all_bookings(self) -> list[Bookings]:
        return await self.repository.get_all_bookings()


booking_service = BookingService()
