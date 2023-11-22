from pydantic import BaseModel
from decimal import Decimal


class Room(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str | None
    services: list | None
    price: Decimal
    quantity: int
    image_id: int
    total_cost: Decimal
    # rooms_left: int  TODO

    class Config:
        from_attributes = True


class GetRoomsResponse(BaseModel):
    rooms: list[Room]
