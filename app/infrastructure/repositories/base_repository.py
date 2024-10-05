from abc import ABC
from typing import TypeVar, Any

from sqlalchemy.ext.asyncio import AsyncSession


T = TypeVar("T")


class BaseRepository[T](ABC):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, obj: T) -> T:
        raise NotImplementedError()

    async def update(self, id: int, value: Any) -> T:
        raise NotImplementedError()

    async def delete(self, id: int) -> T:
        raise NotImplementedError()

    async def get_all(self) -> T:
        raise NotImplementedError()

    async def get_by_id(self, id: int) -> T:
        raise NotImplementedError()