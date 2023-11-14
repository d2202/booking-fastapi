from decimal import Decimal
from datetime import date

from pydantic import BaseModel
from pydantic.v1 import root_validator


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


class PostAddNewBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

    class Config:
        from_attributes = True

    @root_validator(pre=True)
    def validate_all(cls, values):
        print(f"{values}")
        # TODO: пофиксить сравнение date_from и date_to
        return values

