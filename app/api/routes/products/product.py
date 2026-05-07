from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db
from app.db.model.product_model import ProductModel
from app.schemas.product.product_schema import ProductCreate, ProductResponse
from app.services.product.product_service import ProductService

router = APIRouter(prefix="/products", tags=["products"])


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=201,
)
async def create_product(
    product: ProductCreate, db: AsyncSession = Depends(get_db)
) -> ProductModel:
    product_service = ProductService(db)
    return await product_service.create_product(product)
