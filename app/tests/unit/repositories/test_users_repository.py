import pytest
from app.src.repositories.users_repository import users_repository


@pytest.mark.parametrize(
    "email, is_exist",
    [
        ("test@test.com", True),  # user from mock data
        ("some_guy@test.com", False),
    ],
)
async def test_find_user_by_email(email: str, is_exist: bool) -> None:  # from mock data
    user = await users_repository.get_user_by_email(email=email)
    if is_exist:
        assert user is not None
        assert user.id
        assert user.email == email
    else:
        assert user is None


async def test_user_add() -> None:
    email = "user@email.com"
    password = "sup3rs3cr3t"
    await users_repository.add_new_user(email=email, hashed_passwd=password)
