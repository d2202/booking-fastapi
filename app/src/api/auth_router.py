from fastapi import APIRouter, Response, status, HTTPException, Depends

from app.src.api.dependencies import get_current_user, get_current_admin_user
from app.src.models.users import Users
from app.src.schemas.users_schema import PostUserAuthRequest, PostUserAuthResponse, GetUserResponse, GetUsersAllResponse
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


@router.post("/logout")
async def post_logout_user(response: Response) -> dict:
    response.delete_cookie(key="booking_access_token")
    return {"status": "success"}


@router.get("/me")
async def get_user_me(current_user: Users = Depends(get_current_user)) -> GetUserResponse:
    return GetUserResponse(id=current_user.id, email=current_user.email)


@router.get("/all")
async def get_users_all(current_user: Users = Depends(get_current_admin_user)) -> GetUsersAllResponse:
    users_list = await users_service.get_all_users()
    return GetUsersAllResponse(users=users_list)
