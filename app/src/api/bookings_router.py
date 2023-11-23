from fastapi import APIRouter, Depends, status, Response

from app.src.api.dependencies import get_current_user
from app.src.models.users import Users
from app.src.schemas.bookings_schema import (
    GetAllBookingsResponse,
    Booking,
    PostAddNewBooking,
)
from app.src.services.booking_service import booking_service

router = APIRouter(prefix="/api/v1/bookings", tags=["Bookings"])


@router.get("/")
async def get_user_bookings(user: Users = Depends(get_current_user)) -> list[Booking]:
    return await booking_service.get_user_bookings(user_id=user.id)


@router.delete("/{booking_id}")
async def delete_user_booking(
    booking_id: int, user: Users = Depends(get_current_user)
) -> Response:
    await booking_service.delete_user_booking(user_id=user.id, booking_id=booking_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/all")
async def get_all_bookings() -> GetAllBookingsResponse:
    result = await booking_service.get_all_bookings()
    return GetAllBookingsResponse(bookings=result)


@router.post("/add")
async def post_add_booking(
    request_data: PostAddNewBooking, user: Users = Depends(get_current_user)
) -> Response:
    await booking_service.add_booking(
        user_id=user.id,
        room_id=request_data.room_id,
        date_from=request_data.date_from,
        date_to=request_data.date_to,
    )
    return Response(status_code=status.HTTP_201_CREATED)
