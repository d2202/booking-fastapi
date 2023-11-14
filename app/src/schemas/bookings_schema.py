from decimal import Decimal
from datetime import date

from pydantic import BaseModel, root_validator


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

    @root_validator(pre=True)
    def validate_dates(cls, values):
        date_to = values.get("date_to")
        date_from = values.get("date_from")
        if date_from > date_to:
            raise ValueError("Дата выезда не может быть больше даты заезда")
        if date_from == date_to:
            raise ValueError("Даты заезда и выезда не могут быть одинаковыми")
        return values
