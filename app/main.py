import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.infrastructure.di_containers import ServiceContainer
from app.api.middlewares.inject_middleware import UserInjectMiddleware
from app.injectors.user_injectors import get_user_service
from config import config
from api.handlers.handlers import router as main_router


logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


async def main():
    container = ServiceContainer()
    container.init_resources()
    container.wire(
        packages=[
            "api"
        ],
        modules=[
            "api.handlers.handlers",
            "api.middlewares"
        ]
    )
    dp.include_router(main_router)
    main_router.message.middleware(
        UserInjectMiddleware(await get_user_service())
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())