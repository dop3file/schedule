from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel


class UserIn(BaseModel):
    class Config:
        from_attributes = True

    telegram_id: int
    telegram_username: str


class UserOut(BaseModel):
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


class TimeWindow(BaseModel):
    id: int
    left_time_border: str
    right_time_border: str


class Teacher(BaseModel):
    fullname: str


class LessonOut(BaseModel):
    name: str
    time_window: TimeWindow
    teacher: Teacher
    lesson_type: str
    audience: str
