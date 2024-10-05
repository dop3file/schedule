from aiogram import Router

from app.api.middlewares.inject_middleware import InjectMiddleware
from app.api.middlewares.register_middleware import RegisterUserMiddleware
from app.injectors.user_injectors import get_user_service


async def setup_middlewares(router: Router) -> None:
    user_service = await get_user_service()
    router.callback_query.middleware(
        InjectMiddleware(user_service)
    )
    router.message.middleware(
        RegisterUserMiddleware(user_service)
    )
    router.message.middleware(
        InjectMiddleware(user_service)
    )