from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.domain.constants import CHOOSE_GROUP_TEXT


async def get_start_default_keyboard() -> ReplyKeyboardMarkup:
    button_hi = KeyboardButton(text=CHOOSE_GROUP_TEXT)

    keyboard = ReplyKeyboardMarkup(keyboard=[])
    keyboard.add(button_hi)

    return keyboard
