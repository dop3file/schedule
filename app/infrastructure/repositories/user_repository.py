from typing import Optional

from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.exceptions import DBError
from app.infrastructure.models import User
from app.domain.schemas import UserInDTO


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user: UserInDTO) -> None:
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

    async def get_user_by_telegram_id(self, telegram_id: int) -> Optional[User]:
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