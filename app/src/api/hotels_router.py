from fastapi import APIRouter, Depends

from app.src.schemas.hotels_schema import GetHotelsResponse, GetHotelsRequestArgs
from app.src.services.hotels_service import hotels_service

router = APIRouter(
    prefix="/hotels",
    tags=["Hotels and rooms"],
)


@router.get("/")
async def get_hotels(request: GetHotelsRequestArgs = Depends()) -> GetHotelsResponse:
    hotels = await hotels_service.get_hotels_by_location(
        location=request.location,
        date_from=request.date_from,
        date_to=request.date_to
    )
    return GetHotelsResponse(hotels=hotels)
