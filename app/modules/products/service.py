from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.products.model import ProductModel
from app.modules.products.repository import ProductRepository
from app.modules.products.schemas import ProductCreate


class ProductService:
    def __init__(self, db: AsyncSession):
        self.product_repository = ProductRepository(db)

    async def create_product(self, product: ProductCreate) -> ProductModel:
        return await self.product_repository.create(product.model_dump())
