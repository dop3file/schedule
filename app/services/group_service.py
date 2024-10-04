import logging
from typing import Optional

from app.domain.exceptions import DBError, UserNotFoundError
from app.infrastructure.repositories.group_repository import GroupRepository
from app.domain.schemas import GroupOut


class GroupService:
    def __init__(self, group_repository: GroupRepository) -> None:
        self.group_repository = group_repository

    async def get_all(self) -> list[GroupOut]:
        try:
            groups = await self.group_repository.get_all()
            return [GroupOut.from_orm(group) for group in groups]
        except DBError as e:
            logging.debug(e, exc_info=True)
            raise UserNotFoundError from e