from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as keyboards
from app.requests import ShopService

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Создание пользователя в БД если его нет
    await ShopService.set_user(message.from_user.id)
    await message.answer(f"Добро пожаловать в магазин!", reply_markup=keyboards.menu)


@router.message(Command('help'))
async def get_help(message: Message) -> None:
    """Помощь по командам бота"""
    await message.answer(f""" помощь по командам бота:
    /start - Стартовое меню
    /help - помощь по командам бота
    /create_db - создать таблицы в БД
    """)


@router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery) -> None:
    """Каталог товаров"""
    await callback.message.edit_text("Выберите категорию", reply_markup=await keyboards.categories())


@router.callback_query(F.data.startswith("category_"))
async def category(callback: CallbackQuery) -> None:
    """Каталог товаров"""
    await callback.message.edit_text(
        text="Выберите товар",
        reply_markup=await keyboards.get_items(callback.data.split("_")[1])
    )

@router.callback_query(F.data.startswith("item_"))
async def item_handler(callback: CallbackQuery) -> None:
    """Каталог товаров"""
    item = await ShopService.get_item(callback.data.split("_")[1])
    await callback.message.edit_text(
        text=f"{item.name}\n{item.description}\n{item.price} руб.",
        reply_markup=await keyboards.back_to_category(item.category_id)
    )

@router.callback_query(F.data == "start")
async def callback_start(callback: CallbackQuery) -> None:
    await callback.message.edit_text("Главное меню", reply_markup=keyboards.menu)
