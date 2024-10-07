from aiogram.filters import BaseFilter
from aiogram.types import Message


class Text(BaseFilter):
    def __init__(self, text: str | None = None, startswith: str | None = None, texts: list[str] | None = None) -> None:
        self.text = text
        self.startswith = startswith
        self.texts = texts

    async def __call__(self, message: Message) -> bool:
        if self.texts:
            return self.texts_handler(message)
        msg_text = message.text if isinstance(message, Message) else message.data
        if self.startswith:
            return msg_text.startswith(self.startswith)
        return msg_text == self.text

    def texts_handler(self, message: Message) -> bool:
        return message.text in self.texts


