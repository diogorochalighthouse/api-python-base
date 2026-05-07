from sqlalchemy.ext.asyncio import AsyncSession

from app.db.model.product_model import ProductModel
from app.repositories.product.product_repository import ProductRepository
from app.schemas.product.product_schema import ProductCreate


class ProductService:
    def __init__(self, db: AsyncSession):
        self.product_repository = ProductRepository(db)

    async def create_product(self, product: ProductCreate) -> ProductModel:
        return await self.product_repository.create(product.model_dump())
