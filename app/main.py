import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.api.middlewares.register_middleware import RegisterUserMiddleware
from app.infrastructure.di_containers import ServiceContainer
from app.api.middlewares.inject_middleware import UserInjectMiddleware
from app.injectors.user_injectors import get_user_service
from app.utils.middlewares import setup_middlewares
from app.utils.routers import include_routers
from app.utils.setup_di_container import setup_di_containers
from config import config
from api.handlers.user_handlers import router as main_router


logging.basicConfig(level=logging.DEBUG)
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


async def main():
    setup_di_containers()
    await include_routers(dp)
    await setup_middlewares(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())