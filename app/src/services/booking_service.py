from app.src.models.bookings import Bookings
from app.src.repositories.booking_repository import booking_repository
from datetime import date


class BookingService:
    def __init__(self):
        self.repository = booking_repository

    async def add_booking(
        self, user_id: int, room_id: int, date_from: date, date_to: date
    ):
        await self.repository.add_booking(
            user_id=user_id, room_id=room_id, date_from=date_from, date_to=date_to
        )

    async def get_all_bookings(self) -> list[Bookings]:
        return await self.repository.get_all_bookings()

    async def get_user_bookings(self, user_id: int) -> list[Bookings]:
        return await self.repository.get_by_user_id(user_id=user_id)

    async def delete_user_booking(self, user_id: int, booking_id: int):
        await self.repository.delete_booking_by_id(
            user_id=user_id, booking_id=booking_id
        )


booking_service = BookingService()
