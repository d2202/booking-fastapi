from app.src.api.auth import get_password_hash
from app.src.repositories.users_repository import users_repository


class UsersService:
    def __init__(self):
        self.repository = users_repository

    async def register_user(self, email: str, password: str) -> None:
        existing_user = await self.repository.get_by_email(email=email)
        if not existing_user:
            hashed_passwd = get_password_hash(password=password)
            await self.repository.add_new_user(email=email, hashed_passwd=hashed_passwd)


users_service = UsersService()
