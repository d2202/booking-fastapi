from pydantic import BaseModel, EmailStr


class PostRegisterUserRequest(BaseModel):
    email: EmailStr
    password: str
