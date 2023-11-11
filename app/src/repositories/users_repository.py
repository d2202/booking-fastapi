from app.src.models.users import Users
from app.src.repositories.base_repository import BaseRepository


class UsersRepository(BaseRepository):
    model = Users

    async def get_user_by_id(self, user_id: int) -> Users:
        # TODO: return users email and id
        return await self.get_by_id(model_id=user_id)

    async def get_user_by_email(self, email: str) -> Users:
        return await self.find_one_or_none(email=email)

    async def add_new_user(self, email: str, hashed_passwd: str) -> None:
        await self.add(email=email, hashed_password=hashed_passwd)


users_repository = UsersRepository()
