import logging
from typing import Optional

from app.domain.exceptions import DBError, UserNotFoundError, GroupError
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
            raise GroupError from e

    async def get_all_names(self) -> list[GroupOut]:
        try:
            group_names = await self.group_repository.get_all_names()
            return [GroupOut.from_orm(group) for group in group_names]
        except DBError as e:
            logging.debug(e, exc_info=True)
            raise GroupError from e

    async def get(self, id: int) -> GroupOut:
        try:
            group = await self.group_repository.get_by_id(id)
            return GroupOut.from_orm(group)
        except DBError as e:
            logging.debug(e, exc_info=True)
            raise GroupError from e

    async def get_all_subgroups(self, name: str) -> list[GroupOut]:
        try:
            subgroups = await self.group_repository.get_all_by_name(name)
            return [GroupOut.from_orm(subgroup) for subgroup in subgroups]
        except DBError as e:
            logging.debug(e, exc_info=True)
            raise GroupError from e
