from typing import AsyncGenerator, Any

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from config import settings

DATABASE_URL = settings.DATABASE_URL

async_engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass


# async def get_session() -> AsyncGenerator[AsyncSession, Any]:
#     async with async_session() as session:
#         yield session


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)