from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db
from app.modules.products.model import ProductModel
from app.modules.products.schemas import ProductCreate, ProductResponse
from app.modules.products.service import ProductService

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductResponse, status_code=201)
async def create_product(
    product: ProductCreate, db: AsyncSession = Depends(get_db)
) -> ProductModel:
    product_service = ProductService(db)
    return await product_service.create_product(product)
