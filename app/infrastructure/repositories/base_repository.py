from abc import ABC, abstractmethod
from typing import TypeVar, Any

from sqlalchemy.ext.asyncio import AsyncSession


T = TypeVar("T")


class BaseRepository[T](ABC):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, obj: T) -> T:
        raise NotImplemented()

    async def update(self, id: int, value: Any) -> T:
        raise NotImplemented()

    async def delete(self, id: int) -> T:
        raise NotImplemented()

    async def get_all(self) -> T:
        raise NotImplemented()

    async def get_by_id(self, id: int) -> T:
        raise NotImplemented()