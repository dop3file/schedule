import logging

from app.domain.exceptions import DBError, LessonError
from app.domain.schemas import DayIn, LessonOut, TimeWindow
from app.infrastructure.repositories.base_repository import BaseRepository
from app.infrastructure.repositories.lesson_repository import LessonRepository


class DayService(BaseRepository):
    def __init__(self, lesson_repository: LessonRepository):
        self.lesson_repository = lesson_repository

    async def create(self, day: DayIn) -> None:
        try:
            await self.lesson_repository.create_day(day)
        except DBError as e:
            logging.error(e)
            raise LessonError from e

    async def get_all(self) -> list[str]:
        try:
            days = await self.lesson_repository.get_all_days()
            return [day.name for day in days]
        except DBError as e:
            logging.error(e)
            raise LessonError from e


class LessonService(BaseRepository):
    def __init__(self, lesson_repository: LessonRepository):
        self.lesson_repository = lesson_repository

    async def get_lessons_from_day(
        self,
        group_id: int,
        day_id: int,
    ) -> list[LessonOut]:
        try:
            lessons = await self.lesson_repository.get_lessons_from_day(
                group_id=group_id,
                day_id=day_id,
                is_underscore=True
            )

            return [LessonOut.from_orm(lesson) for lesson in lessons]
        except DBError as e:
            logging.error(e)
            raise LessonError

    async def create_time_window(self, time_window: TimeWindow) -> None:
        await self.lesson_repository.create_time_window(
            **time_window.dict()
        )

