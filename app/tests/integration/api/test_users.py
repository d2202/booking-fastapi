import pytest
from httpx import AsyncClient
from fastapi import status


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("supertest@test.com", "test", status.HTTP_201_CREATED),
        ("supertest@test.com", "test123", status.HTTP_409_CONFLICT),
        ("asdvxv", "test123", status.HTTP_422_UNPROCESSABLE_ENTITY),
    ],
)
async def test_register_user(
    client: AsyncClient, email: str, password: str, status_code: int
) -> None:
    response = await client.post(
        url="/auth/register", json={"email": email, "password": password}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("test@test.com", "test", status.HTTP_200_OK),
        ("some_guy@test.com", "test123", status.HTTP_401_UNAUTHORIZED),
    ],
)
async def test_login_user(
    client: AsyncClient, email: str, password: str, status_code: int
) -> None:
    response = await client.post(
        url="/auth/login", json={"email": email, "password": password}
    )
    assert response.status_code == status_code
