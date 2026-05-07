from fastapi import APIRouter

from app.api.routes.health.health import router as health_router
from app.api.routes.users.user import router as users_router
from app.api.routes.products.product import router as products_router

router = APIRouter()

router.include_router(health_router)
router.include_router(users_router)
router.include_router(products_router)
