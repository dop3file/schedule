from typing import Optional

from sqlalchemy import insert, select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.exceptions import DBError
from app.domain.schemas import UserIn
from app.infrastructure.repositories.base_repository import BaseRepository
from app.infrastructure.models import User


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: UserIn) -> None:
        try:
            stmt = insert(
                    User,
                ).values(
                    telegram_id=user.telegram_id,
                    telegram_username=user.telegram_username,
                )
            await self.session.execute(stmt)
            await self.session.commit()
        except SQLAlchemyError as e:
            raise DBError from e

    async def get_by_telegram_id(self, telegram_id: int) -> Optional[User]:
        try:
            stmt = select(
                    User,
                ).where(
                    User.telegram_id == telegram_id
                )

            result = await self.session.execute(stmt)
            return result.scalar()
        except SQLAlchemyError as e:
            raise DBError from e

    async def update_user_group_id(self, user_id: int, group_id: int) -> None:
        try:
            async with self.session.begin():
                stmt = update(
                    User,
                ).where(
                    User.id == user_id
                ).values(
                    group_id=group_id
                )
                await self.session.execute(stmt)
                await self.session.commit()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise DBError from e

    def delete(self, user_id: int) -> None:
        pass

    def get_all(self) -> list[User]:
        pass

    def get_by_id(self, id: int) -> User:
        ...