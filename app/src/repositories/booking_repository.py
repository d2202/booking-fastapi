from sqlalchemy import select, and_, or_, func

from app.src.api.exceptions import (
    BookingErrorException,
    RoomNotFoundError,
    BookingNotFoundException,
)
from app.src.models.bookings import Bookings
from app.src.models.db import async_session_maker
from app.src.models.rooms import Rooms
from app.src.repositories.base_repository import BaseRepository
from datetime import date


class BookingRepository(BaseRepository):
    model = Bookings

    async def check_booking_available(
        self, room_id: int, date_from: date, date_to: date
    ):
        async with async_session_maker() as session:
            booked_rooms = (
                select(Bookings)
                .where(
                    and_(
                        Bookings.room_id == room_id,
                        or_(
                            and_(
                                Bookings.date_from >= date_from,
                                Bookings.date_from <= date_to,
                            ),
                            and_(
                                Bookings.date_from <= date_from,
                                Bookings.date_to <= date_from,
                            ),
                        ),
                    )
                )
                .cte("booked_rooms")
            )

            get_rooms_left = (
                select(
                    (Rooms.quantity - func.count(booked_rooms.c.room_id)).label(
                        "rooms_left"
                    )
                )
                .select_from(Rooms)
                .join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True)
                .where(Rooms.id == room_id)
                .group_by(Rooms.quantity, booked_rooms.c.room_id)
            )
            rooms_left = (await session.execute(get_rooms_left)).scalar()
            if rooms_left is None:
                raise RoomNotFoundError
            return rooms_left > 0

    async def add_booking(
        self, user_id: int, room_id: int, date_from: date, date_to: date
    ):
        is_booking_available = await self.check_booking_available(
            room_id=room_id, date_from=date_from, date_to=date_to
        )
        if is_booking_available:
            async with async_session_maker() as session:
                get_price_query = select(Rooms.price).filter_by(id=room_id)
                price: int = (await session.execute(get_price_query)).scalar()
                await self.add(
                    user_id=user_id,
                    room_id=room_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price,
                )
        else:
            raise BookingErrorException

    async def get_all_bookings(self) -> list[Bookings]:
        return await self.get_all()

    async def get_by_user_id(self, user_id: int) -> list[Bookings]:
        return await self.get_by_filter(user_id=user_id)

    async def delete_booking_by_id(self, user_id: int, booking_id: int) -> None:
        booking = await self.get_by_filter(user_id=user_id, id=booking_id)
        if booking:
            async with async_session_maker() as session:
                await session.delete(booking)
                session.commit()
        raise BookingNotFoundException


booking_repository = BookingRepository()
