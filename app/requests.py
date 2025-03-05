from sqlalchemy import select

from app.database.database import async_session
from app.database.models import User, Category, Item


class ShopService:

    @classmethod
    async def set_user(cls, tg_id: int) -> None:
        """Создание пользователя в БД если его нет"""
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            if not user:
                user = User(tg_id=tg_id)
                session.add(user)
                await session.commit()

    @classmethod
    async def get_categories(cls) -> list[str]:
        """Получение категорий товаров"""
        async with async_session() as session:
            categories = await session.scalars(select(Category))
            return categories

    @classmethod
    async def get_items_by_category(cls, category_id: int) -> list[str]:
        """Получение товаров по категории"""
        async with async_session() as session:
            items = await session.scalars(select(Item).where(Item.category_id == category_id))
            return items


    @classmethod
    async def get_item(cls, item_id: int) -> list[str]:
        """Получение товара по id"""
        async with async_session() as session:
            item = await session.scalar(select(Item).where(Item.id == item_id))
            return item


