from httpx import AsyncClient
from fastapi import status
from app.src.services.booking_service import booking_service
from app.src.services.users_service import users_service


async def test_get_user_bookings(authenticated_client: AsyncClient) -> None:
    user = await users_service.get_by_email(email="test@test.com")
    assert user

    bookings_count = len(await booking_service.get_user_bookings(user_id=user.id))

    response = await authenticated_client.get(
        url="/api/v1/bookings/",
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() is not None
    assert len(response.json()) == bookings_count
