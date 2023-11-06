from fastapi import APIRouter, Response, status

from app.src.schemas.users_schema import PostRegisterUserRequest
from app.src.services.users_service import users_service

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"]
)


@router.post("/register")
async def post_register_user(data: PostRegisterUserRequest) -> Response:
    await users_service.register_user(email=data.email, password=data.password)
    return Response(status_code=status.HTTP_201_CREATED)
