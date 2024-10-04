from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from app.domain.constants import CHOOSE_GROUP_BUTTON_TEXT


async def get_start_default_keyboard() -> ReplyKeyboardMarkup:
    button_hi = KeyboardButton(text=CHOOSE_GROUP_BUTTON_TEXT)

    keyboard = ReplyKeyboardMarkup(keyboard=[])
    keyboard.add(button_hi)

    return keyboard
