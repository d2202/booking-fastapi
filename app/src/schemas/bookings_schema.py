from decimal import Decimal
from datetime import date

from pydantic import BaseModel


class Booking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: Decimal
    total_cost: Decimal
    total_days: int

    class Config:
        from_attributes = True


class GetAllBookingsResponse(BaseModel):
    bookings: list[Booking]
