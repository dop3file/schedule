from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.exceptions import DBError, GroupNotFoundError
from app.infrastructure.models import Group
from app.infrastructure.repositories.base_repository import BaseRepository


class GroupRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> Sequence[Group]:
        try:
            stmt = select(Group)

            result = await self.session.execute(stmt)
            return result.scalars().all()
        except SQLAlchemyError as e:
            raise DBError from e

    async def get_all_names(self) -> Sequence[Group]:
        try:
            stmt = select(Group).distinct(Group.name)
            result = await self.session.execute(stmt)
            return result.scalars().all()
        except SQLAlchemyError as e:
            raise DBError from e

    async def get_by_id(self, id: int) -> Group:
        try:
            stmt = select(Group).where(Group.id == id)
            result = await self.session.execute(stmt)
            group = result.scalars().first()
            if group is None:
                raise GroupNotFoundError()
            return group
        except SQLAlchemyError as e:
            raise DBError from e

    async def get_all_by_name(self, name: str) -> Sequence[Group]:
        try:
            stmt = select(Group).where(Group.name == name)
            result = await self.session.execute(stmt)
            groups = result.scalars().all()
            return groups
        except SQLAlchemyError as e:
            raise DBError from e