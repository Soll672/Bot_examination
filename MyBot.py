import asyncio
from aiogram import Bot, Dispatcher
from handlers.start_handler import start_router
from handlers.homework_handler import homework_router
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


dp.include_router(start_router)
dp.include_router(homework_router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

