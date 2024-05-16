import asyncio
from aiogram import Bot, Dispatcher
from aiogram
from token import token

bot = Bot(token = token)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())