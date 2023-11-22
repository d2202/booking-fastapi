from app.src.api.hotels_router import router
from app.src.schemas.rooms_schemas import GetRoomsResponse
from app.src.services.rooms_service import rooms_service


@router.get("/{hotel_id}/rooms")
async def get_rooms(hotel_id: int) -> GetRoomsResponse:
    rooms = await rooms_service.get_rooms_by_hotel_id(hotel_id=hotel_id)
    return GetRoomsResponse(rooms=rooms)
