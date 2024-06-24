import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from app.handlers import router

TELEGRAM_BOT_TOKEN = "7404403100:AAHxn7iAEN-g8LzpZFOqTCW1Z_KEsEO3kwQ"
logging.basicConfig(level=logging.INFO)


async def main():
    storage = MemoryStorage()
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(storage=storage)
    dp.include_router(router)

    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logging.warning("Bot has been turned off")


if __name__ == "__main__":
    asyncio.run(main())
