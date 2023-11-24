from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from app.src.schemas.hotels_schema import GetHotelsResponse, GetHotelsRequestArgs, Hotel
from app.src.services.hotels_service import hotels_service

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels and rooms"],
)


@router.get("/")
@cache(expire=60)
async def get_hotels(
    request_data: GetHotelsRequestArgs = Depends()
) -> GetHotelsResponse:
    hotels = await hotels_service.get_hotels_by_location(
        location=request_data.location,
        date_from=request_data.date_from,
        date_to=request_data.date_to,
    )
    return GetHotelsResponse(hotels=hotels)


@router.get("/id/{hotel_id}")
async def get_hotel_by_id(hotel_id: int) -> Hotel:
    hotel_data = await hotels_service.get_by_hotel_id(hotel_id=hotel_id)
    return Hotel(**hotel_data)
