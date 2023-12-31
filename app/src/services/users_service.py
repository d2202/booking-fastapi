from app.src.auth import get_password_hash, verify_password, create_access_token
from app.src.api.exceptions import (
    UserAlreadyExistsException,
    IncorrectUserDataException,
)
from app.src.models.users import Users
from app.src.repositories.users_repository import users_repository


class UsersService:
    def __init__(self):
        self.repository = users_repository

    async def get_all_users(self) -> list[Users]:
        return await self.repository.get_all()

    async def get_by_id(self, user_id: int) -> Users:
        return await self.repository.get_by_id(model_id=user_id)

    async def get_by_email(self, email: str) -> Users:
        return await self.repository.find_one_or_none(email=email)

    async def register_user(self, email: str, password: str) -> None:
        existing_user = await self.repository.get_user_by_email(email=email)
        if existing_user:
            raise UserAlreadyExistsException
        hashed_passwd = get_password_hash(password=password)
        await self.repository.add_new_user(email=email, hashed_passwd=hashed_passwd)

    async def login_user(self, email: str, password: str) -> str:
        existing_user = await self.repository.get_user_by_email(email=email)
        if existing_user:
            is_valid_password = verify_password(password, existing_user.hashed_password)
            if is_valid_password:
                access_token = create_access_token(data={"sub": str(existing_user.id)})
                return access_token
        raise IncorrectUserDataException


users_service = UsersService()
