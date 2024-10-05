import logging
from typing import Optional

from app.domain.exceptions import DBError, CreateUserError, UserNotFoundError, UserError
from app.infrastructure.repositories.user_repository import UserRepository
from app.domain.schemas import UserInDTO, UserOutDTO


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def create_user(self, user: UserInDTO) -> None:
        try:
            if await self.user_repository.get_by_telegram_id(user.telegram_id) is not None:
                return
            await self.user_repository.create(user)
        except DBError as e:
            logging.debug(e, exc_info=True)
            raise CreateUserError from e

    async def get_user(self, user: UserInDTO) -> Optional[UserOutDTO]:
        try:
            user = await self.user_repository.get_by_telegram_id(user.telegram_id)
            if user is None:
                return None
            return UserOutDTO.from_orm(user)
        except DBError as e:
            logging.debug(e, exc_info=True)
            raise UserNotFoundError from e

    async def update_user_group(self, user: UserInDTO, group_id: int) -> None:
        try:
            user = await self.user_repository.get_by_telegram_id(user.telegram_id)
            if user is None:
                return None
            await self.user_repository.update_user_group_id(user.id, group_id)
        except DBError as e:
            logging.debug(e, exc_info=True)
            raise UserError from e