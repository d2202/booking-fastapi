from app.src.models.bookings import Bookings
from app.src.repositories.booking_repository import booking_repository


class BookingService:
    def __init__(self):
        self.repository = booking_repository

    async def get_all_bookings(self) -> list[Bookings]:
        return await self.repository.get_all_bookings()

    async def get_user_bookings(self, user_id: int) -> list[Bookings]:
        return await self.repository.get_by_user_id(user_id=user_id)


booking_service = BookingService()
