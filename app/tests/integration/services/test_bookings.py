import datetime

from app.src.services.booking_service import booking_service


async def test_add_and_get_booking() -> None:
    bookings_count = len(await booking_service.get_user_bookings(user_id=2))
    assert bookings_count == 1
    await booking_service.add_booking(
        user_id=2,
        room_id=2,
        date_from=datetime.date.today(),
        date_to=datetime.date.today() + datetime.timedelta(days=2),
    )
    bookings_count_after = len(await booking_service.get_user_bookings(user_id=2))
    assert bookings_count_after == 2
