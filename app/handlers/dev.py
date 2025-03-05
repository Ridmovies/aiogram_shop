from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.database.database import create_tables

dev_router = Router()


@dev_router.message(Command('create_db'))
async def create_database(message: Message) -> None:
    await create_tables()
    await message.answer("Create tables!!!")
