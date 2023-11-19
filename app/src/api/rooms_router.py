from app.src.api.hotels_router import router


@router.get("/{hotel_id}/rooms")
async def get_rooms():
    pass
