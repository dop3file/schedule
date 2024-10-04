import logging
from pprint import pprint
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from dependency_injector.wiring import inject, Provide

from app.domain.schemas import UserInDTO
from app.services.user_service import UserService


@inject
class UserInjectMiddleware(BaseMiddleware):
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user = data["event_from_user"]
        user_in = UserInDTO(
            telegram_id=user.id,
            telegram_username=user.username
        )
        data["user_out"] = await self.user_service.get_user(user_in)
        data["user_in"] = user_in
        result = await handler(event, data)
        return result
