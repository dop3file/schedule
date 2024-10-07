from aiogram import Router
from aiogram.types import Message

from app.api.filters import Text
from app.domain.constants import DAYS
from app.domain.controllers import build_schedule_day_text
from app.domain.schemas import UserOut
from app.services.lesson_service import LessonService

router = Router()


@router.message(Text(texts=DAYS))
async def schedule(
    message: Message,
    user_out: UserOut,
    lesson_service: LessonService
):
    day_id = DAYS.index(message.text) + 1
    lessons = await lesson_service.get_lessons_from_day(
        day_id=day_id,
        group_id=user_out.group_id
    )
    await message.answer(
        build_schedule_day_text(lessons)
    )