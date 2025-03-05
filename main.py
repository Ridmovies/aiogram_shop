import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from config import settings
from app.handlers.main import router
from app.handlers.dev import dev_router

# Bot token can be obtained via https://t.me/BotFather
TOKEN = settings.BOT_TOKEN

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


async def main() -> None:
    dp.include_router(router)
    dp.include_router(dev_router)
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())