import logging
from typing import Sequence

from sqlalchemy import select, insert, or_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.exceptions import DBError
from app.domain.schemas import DayIn
from app.infrastructure.models import Day, Lesson, TimeWindow
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

    async def create_day(self, day_in: DayIn) -> None:
        try:
            async with self.session.begin():
                stmt = insert(
                        Day
                    ).values(
                    id=day_in.id,
                    name=day_in.name
                )
                await self.session.execute(stmt)
                await self.session.commit()
        except SQLAlchemyError:
            ...

    async def get_lessons_from_day(
        self,
        group_id: int,
        day_id: int,
        is_underscore: bool
    ) -> Sequence[Lesson]:
        try:
            async with (self.session.begin()):
                stmt = select(
                        Lesson
                ).where(
                    Lesson.group_id == group_id,
                    Lesson.day_id == day_id,
                    or_(
                        Lesson.is_underscore == is_underscore,
                        Lesson.is_underscore is None
                    )
                ).order_by(Lesson.time_window_id)
                result = await self.session.execute(stmt)
                return result.scalars().all()
        except SQLAlchemyError:
            ...

    async def create_time_window(
        self,
        id: int,
        left_time_border: str,
        right_time_border: str
    ) -> None:
        try:
            async with (self.session.begin()):
                stmt = insert(
                    TimeWindow
                ).values(
                    id=id,
                    left_time_border=left_time_border,
                    right_time_border=right_time_border
                )
                await self.session.execute(stmt)
        except SQLAlchemyError as e:
            logging.debug(e)