from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.database import Base


class Group(Base):
    """Group model for university group."""

    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    subgroup: Mapped[int]
    users: Mapped[List["User"]] = relationship(back_populates="group")


class User(Base):
    """User model for every telegram user."""

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    telegram_id: Mapped[int] = mapped_column(index=True)
    telegram_username: Mapped[str] = mapped_column(unique=True)
    group_id: Mapped[int] = mapped_column(ForeignKey(Group.id), nullable=True)
    group: Mapped["Group"] = relationship(back_populates="users")


class TimeWindow(Base):
    """Time Window model for numbering by lessons (for example first lesson 8:20 - 9:45)"""

    __tablename__ = 'time_windows'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    left_time_border: Mapped[datetime]
    right_time_border: Mapped[datetime]


class Teacher(Base):
    """Teacher model for real teacher from university"""

    __tablename__ = 'teachers'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    fullname: Mapped[str] = mapped_column(nullable=False, index=True)


class LessonType(Base):
    """Lesson type model for real lesson type(for example lecture, labaratory and etc)"""

    __tablename__ = 'lesson_types'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]


class Lesson(Base):
    """Group model for university group."""

    __tablename__ = 'lessons'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    time_window_id: Mapped[int] = mapped_column(ForeignKey(TimeWindow.id))
    is_underscore: Mapped[bool]
    teacher_id: Mapped[int] = mapped_column(ForeignKey(Teacher.id))
    group_id: Mapped[int] = mapped_column(ForeignKey(Group.id))
    lesson_type_id: Mapped[int] = mapped_column(ForeignKey(LessonType.id))
