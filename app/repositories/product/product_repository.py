from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.model.product_model import ProductModel


class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, product_data: dict[str, Any]) -> ProductModel:
        product = ProductModel(**product_data)
        self.db.add(product)
        await self.db.commit()
        await self.db.refresh(product)
        return product
