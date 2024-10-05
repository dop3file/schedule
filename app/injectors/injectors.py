from typing import Any

from app.injectors.group_injectors import get_group_service
from app.injectors.lesson_injectors import get_lesson_service
from app.injectors.user_injectors import get_user_service


async def get_injectors() -> dict[str, Any]:
    return {
        "user_service": get_user_service(),
        "group_service": get_group_service(),
        "lesson_service": get_lesson_service()
    }