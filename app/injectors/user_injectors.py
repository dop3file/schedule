from app.infrastructure.databases.sql_database import get_db_session_context
from app.infrastructure.repositories.user_repository import UserRepository
from app.services.user_service import UserService


async def get_user_service() -> UserService:
    async with get_db_session_context() as session:
        user_service = UserService(
            UserRepository(
                session
            )
        )
        return user_service
