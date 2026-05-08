from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db
from app.modules.users.model import UserModel
from app.modules.users.schemas import UserCreate, UserResponse
from app.modules.users.service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(
    user: UserCreate, db: AsyncSession = Depends(get_db)
) -> UserModel:
    user_service = UserService(db)
    return await user_service.create_user(user)


@router.get("/", response_model=List[UserResponse])
async def list_users(db: AsyncSession = Depends(get_db)) -> list[UserModel]:
    user_service = UserService(db)
    return await user_service.list_users()
