from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from app.api.callback_datas import SELECT_GROUP
from app.domain.schemas import GroupOut


async def get_choosing_group_handler(groups: list[GroupOut]) -> InlineKeyboardMarkup:
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for group in groups:
        inline_keyboard.add(
            InlineKeyboardButton(
                text=group.name,
                callback_data=SELECT_GROUP.format(group.id)
            )
        )

    return inline_keyboard
