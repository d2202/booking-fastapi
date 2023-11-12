import datetime

from fastapi import HTTPException, status, Depends
from starlette.requests import Request
from jose import jwt, JWTError

from app.config import settings
from app.src.models.users import Users
from app.src.services.users_service import users_service


def get_cookies(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token


async def get_current_user(token: str = Depends(get_cookies)):
    try:
        payload = jwt.decode(token=token, key=settings.SERVER_SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    expire = payload.get("exp")
    if expire and (int(expire) >= datetime.datetime.utcnow().timestamp()):
        user_id = payload.get("sub")
        if user_id:
            user = await users_service.get_by_id(user_id=int(user_id))
            if user:
                return user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


async def get_current_admin_user(current_user: Users = Depends(get_current_user)) -> Users:
    if not current_user.is_admin or (current_user.is_admin is None):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return current_user
