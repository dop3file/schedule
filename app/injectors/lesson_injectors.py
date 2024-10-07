from app.infrastructure.databases.sql_database import get_db_session_context
from app.infrastructure.repositories.lesson_repository import LessonRepository
from app.services.lesson_service import LessonService, DayService


async def get_lesson_service() -> LessonService:
    async with get_db_session_context() as session:
        lesson_service = LessonService(
            LessonRepository(
                session
            )
        )
        return lesson_service


async def get_day_service() -> DayService:
    async with get_db_session_context() as session:
        day_service = DayService(
            LessonRepository(
                session
            )
        )
        return day_service
