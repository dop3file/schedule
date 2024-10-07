import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.injectors.lesson_injectors import get_day_service, get_lesson_service
from app.scripts.init_scripts import insert_days, insert_time_windows
from app.utils.middlewares import setup_middlewares
from app.utils.routers import include_routers
from config import config


async def main():
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    await insert_days(
        await get_day_service()
    )
    await insert_time_windows(
        await get_lesson_service()
    )
    await include_routers(dp)
    await setup_middlewares(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())