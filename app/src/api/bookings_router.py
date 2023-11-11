from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.src.api.dependencies import get_current_user
from app.src.models.users import Users
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


@router.get("/user")
async def get_user_bookings(user: Users = Depends(get_current_user)):
    # TODO: return list of Bookings
    return
