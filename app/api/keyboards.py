from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from app.api.callback_datas import SelectGroupCallbackData, SelectSubGroupCallbackData
from app.domain.constants import SETTINGS
from app.domain.schemas import GroupOut, Subgroups


async def get_groups_keyboard(groups: list[GroupOut]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for group in groups:
        builder.row(
            InlineKeyboardButton(
                text=group.name,
                callback_data=SelectGroupCallbackData.callback_data.format(group.id)
            )
        )

    return builder.as_markup()


async def get_subgroups_keyboard(subgroups: Subgroups) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for subgroup, group_id in zip(subgroups.subgroups, subgroups.ids):
        builder.row(
            InlineKeyboardButton(
                text=str(subgroup),
                callback_data=SelectSubGroupCallbackData.callback_data.format(group_id)
            )
        )

    return builder.as_markup()


async def get_main_keyboard(days: list[str]) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()

    for day in days:
        keyboard.add(
            KeyboardButton(
                text=day
            )
        )
    keyboard.add(
        KeyboardButton(
            text=SETTINGS
        )
    )
    keyboard.adjust(3, 5)
    return keyboard.as_markup()
