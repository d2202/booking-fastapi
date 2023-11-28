from app.src.services.users_service import users_service


async def test_get_user_by_email() -> None:
    user = await users_service.get_by_email(email="test@test.com")  # from mocked data
    assert user
