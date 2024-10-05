from aiogram.filters import BaseFilter
from aiogram.types import Message


class Text(BaseFilter):
    def __init__(self, my_text: str | None = None, startswith: str | None = None) -> None:
        self.my_text = my_text
        self.startswith = startswith

    async def __call__(self, message: Message) -> bool:
        msg_text = message.text if isinstance(message, Message) else message.data
        if self.startswith:
            return msg_text.startswith(self.startswith)
        return msg_text == self.my_text


