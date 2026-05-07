from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.model.user_model import UserModel


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user_data: dict[str, Any]) -> UserModel:
        user = UserModel(**user_data)

        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

        return user

    async def get_by_email(self, email: str) -> UserModel | None:
        query = select(UserModel).where(
            UserModel.email == email,
            UserModel.deleted.is_(False),
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def list_users(self) -> list[UserModel]:
        query = select(UserModel).where(
            UserModel.deleted.is_(False),
        )

        result = await self.db.execute(query)
        return list(result.scalars().all())
