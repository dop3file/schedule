from app.infrastructure.databases.sql_database import get_db_session_context
from app.infrastructure.repositories.lesson_repository import LessonRepository
from app.services.lesson_service import LessonService


async def get_lesson_service() -> LessonService:
    async with get_db_session_context() as session:
        lesson_service = LessonService(
            LessonRepository(
                session
            )
        )
        return lesson_service
