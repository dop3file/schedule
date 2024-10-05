from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.exceptions import DBError
from app.infrastructure.models import Day
from app.infrastructure.repositories.base_repository import BaseRepository


class LessonRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_days(self) -> Sequence[Day]:
        try:
            stmt = select(
                    Day
                )

            result = await self.session.execute(stmt)
            return result.scalars().all()
        except SQLAlchemyError as e:
            raise DBError from e