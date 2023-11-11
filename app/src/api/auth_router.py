from fastapi import APIRouter, Response, status, HTTPException

from app.src.schemas.users_schema import PostUserAuthRequest, PostUserAuthResponse
from app.src.services.users_service import users_service, AuthFailedException

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"]
)


@router.post("/register")
async def post_register_user(data: PostUserAuthRequest) -> Response:
    await users_service.register_user(email=data.email, password=data.password)
    return Response(status_code=status.HTTP_201_CREATED)


@router.post("/login")
async def post_auth_user(data: PostUserAuthRequest, response: Response) -> PostUserAuthResponse:
    try:
        access_token = await users_service.login_user(email=data.email, password=data.password)
    except AuthFailedException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return PostUserAuthResponse(access_token=access_token)
