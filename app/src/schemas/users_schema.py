import datetime

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_admin: bool

    class Config:
        from_attributes = True


class PostUserAuthRequest(BaseModel):
    email: EmailStr
    password: str


class PostUserAuthResponse(BaseModel):
    access_token: str


class GetUserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class GetUsersAllResponse(BaseModel):
    users: list[User]
