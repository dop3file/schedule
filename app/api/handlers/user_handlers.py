from typing import Optional

from aiogram import Router, types
from aiogram.filters import Command
from dependency_injector.wiring import inject

from app.api.keyboards import get_groups_keyboard, get_main_keyboard
from app.domain.constants import WELCOME_MESSAGE, CHOOSE_GROUP_TEXT
from app.domain.schemas import UserIn, UserOut
from app.services.group_service import GroupService
from app.services.lesson_service import LessonService, DayService
from app.services.user_service import UserService


router = Router()


async def choosing_group(
    message: types.Message,
    group_service: GroupService
):
    await message.answer(
        CHOOSE_GROUP_TEXT,
        reply_markup=await get_groups_keyboard(
            await group_service.get_all_names()
        )
    )


async def main(
    message: types.Message,
    day_service: DayService
):
    days = await day_service.get_all()
    await message.answer(
        WELCOME_MESSAGE.format(message.from_user.first_name),
        reply_markup=await get_main_keyboard(days)
    )


@router.message(Command("start"))
@inject
async def start(
    message: types.Message,
    user_in: UserIn,
    user_out: Optional[UserOut],
    user_service: UserService,
    group_service: GroupService,
    lesson_service: LessonService,
    day_service: DayService
):
    if user_out.group_id is not None:
        await main(
            message,
            day_service=day_service
        )
    else:
        await choosing_group(
            message,
            group_service=group_service
        )
