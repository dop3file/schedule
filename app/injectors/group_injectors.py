from app.infrastructure.databases.sql_database import get_db_session_context
from app.infrastructure.repositories.group_repository import GroupRepository
from app.services.group_service import GroupService


async def get_group_service() -> GroupService:
    async with get_db_session_context() as session:
        group_service = GroupService(
            GroupRepository(
                session
            )
        )
        return group_service
