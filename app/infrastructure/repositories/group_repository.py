from typing import Optional, Sequence

from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.exceptions import DBError
from app.infrastructure.models import User, Group
from app.domain.schemas import UserInDTO


class GroupRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> Sequence[Group]:
        try:
            stmt = select(Group)

            result = await self.session.execute(stmt)
            return result.scalars().all()
        except SQLAlchemyError as e:
            raise DBError from e