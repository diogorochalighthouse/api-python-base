from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    password: str
    phone: str | None = None


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int
    created_at: datetime
    phone: str | None = None

    model_config = ConfigDict(from_attributes=True)
