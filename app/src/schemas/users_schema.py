from pydantic import BaseModel, EmailStr


class PostUserAuthRequest(BaseModel):
    email: EmailStr
    password: str


class PostUserAuthResponse(BaseModel):
    access_token: str
