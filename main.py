import asyncio

from aiogram import Bot, Dispatcher

from aiogram.methods import DeleteWebhook

from config import TOKEN_API

from app.handlers import router

from database.models import async_main


async def main():
    await async_main()
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher()
    dp.include_router(router)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот отключен!")