import logging

from app.domain.exceptions import DBError, LessonError
from app.domain.schemas import DayIn
from app.infrastructure.repositories.base_repository import BaseRepository
from app.infrastructure.repositories.lesson_repository import LessonRepository


class DayService(BaseRepository):
    def __init__(self, lesson_repository: LessonRepository):
        self.lesson_repository = lesson_repository

    async def create(self, day: DayIn) -> None:
        ...


class LessonService(BaseRepository):
    def __init__(self, lesson_repository: LessonRepository):
        self.lesson_repository = lesson_repository

    async def get_all_days(self) -> list[str]:
        try:
            days = await self.lesson_repository.get_all_days()
            return [day.name for day in days]
        except DBError as e:
            logging.error(e)
            raise LessonError from e