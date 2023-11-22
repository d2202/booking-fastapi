from datetime import date

from pydantic import BaseModel


class GetHotelsRequestArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
    ) -> None:
        self.location = location
        self.date_from = date_from
        self.date_to = date_to


class Hotel(BaseModel):
    id: int
    name: str
    location: str
    services: list
    rooms_quantity: int
    image_id: int | None

    class Config:
        from_attributes = True


class GetHotelsResponse(BaseModel):
    hotels: list[Hotel]
