from fastapi import APIRouter

from app.modules.health.routes import router as health_router
from app.modules.products.routes import router as products_router
from app.modules.users.routes import router as users_router

router = APIRouter()

router.include_router(health_router)
router.include_router(users_router)
router.include_router(products_router)
