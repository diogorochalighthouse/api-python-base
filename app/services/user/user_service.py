from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.model.user_model import UserModel
from app.repositories.user.user_repository import UserRepository
from app.schemas.user.user_schema import UserCreate


class UserService:
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)

    async def create_user(self, user: UserCreate) -> UserModel:
        user_exists = await self.user_repository.get_by_email(user.email)

        if user_exists:
            raise HTTPException(status_code=400, detail="User already exists")

        return await self.user_repository.create(user.model_dump())

    async def list_users(self) -> list[UserModel]:
        return await self.user_repository.list_users()
