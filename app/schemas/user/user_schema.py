from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    password: str


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
