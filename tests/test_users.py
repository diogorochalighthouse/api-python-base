from datetime import datetime, timezone
from unittest.mock import AsyncMock

from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.main import app
from app.modules.users.service import UserService


client = TestClient(app)


def test_create_user_returns_created_user() -> None:
    created_user = {
        "id": "user-1",
        "name": "Alice",
        "email": "alice@example.com",
        "age": 30,
        "phone": "11999999999",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    mocked_create = AsyncMock(return_value=created_user)

    original = UserService.create_user
    UserService.create_user = mocked_create  # type: ignore[method-assign]
    try:
        response = client.post(
            "/users/",
            json={
                "name": "Alice",
                "email": "alice@example.com",
                "age": 30,
                "password": "secret",
                "phone": "11999999999",
            },
        )
    finally:
        UserService.create_user = original

    assert response.status_code == 201
    assert response.json()["email"] == "alice@example.com"
    mocked_create.assert_awaited_once()


def test_create_user_returns_conflict_when_already_exists() -> None:
    mocked_create = AsyncMock(
        side_effect=HTTPException(status_code=400, detail="User already exists")
    )

    original = UserService.create_user
    UserService.create_user = mocked_create  # type: ignore[method-assign]
    try:
        response = client.post(
            "/users/",
            json={
                "name": "Alice",
                "email": "alice@example.com",
                "age": 30,
                "password": "secret",
            },
        )
    finally:
        UserService.create_user = original

    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}


def test_list_users_returns_users() -> None:
    mocked_list = AsyncMock(
        return_value=[
            {
                "id": "user-1",
                "name": "Alice",
                "email": "alice@example.com",
                "age": 30,
                "phone": "11999999999",
                "created_at": datetime.now(timezone.utc).isoformat(),
            }
        ]
    )

    original = UserService.list_users
    UserService.list_users = mocked_list  # type: ignore[method-assign]
    try:
        response = client.get("/users/")
    finally:
        UserService.list_users = original

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["email"] == "alice@example.com"
    mocked_list.assert_awaited_once()
