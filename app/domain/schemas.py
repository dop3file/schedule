from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel


class UserInDTO(BaseModel):
    class Config:
        from_attributes = True

    telegram_id: int
    telegram_username: str


class UserOutDTO(BaseModel):
    class Config:
        from_attributes = True

    id: int
    telegram_id: int
    telegram_username: str
    group_id: Optional[int]


class GroupOut(BaseModel):
    class Config:
        from_attributes = True
        
    id: int
    name: str
    subgroup: int


@dataclass
class Subgroups:
    subgroups: list[int]
    ids: list[int]


class DayIn(BaseModel):
    id: int
    name: str