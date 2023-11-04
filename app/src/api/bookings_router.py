from fastapi import APIRouter

from app.src.schemas.bookings_schema import GetAllBookingsResponse
from app.src.services.booking_service import booking_service

router = APIRouter(
    prefix="/api/v1/bookings",
    tags=["Bookings"]
)


@router.get("/")
async def get_all_bookings() -> GetAllBookingsResponse:
    result = await booking_service.get_all_bookings()
    return GetAllBookingsResponse(bookings=result)
