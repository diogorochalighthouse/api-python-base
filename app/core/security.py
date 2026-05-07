from datetime import datetime, timedelta, timezone
from typing import Any

import jwt

from app.core.config import settings


def create_access_token(data: dict[str, Any]) -> str:
    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(hours=2)

    payload.update(
        {
            "exp": expire,
        }
    )

    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )
