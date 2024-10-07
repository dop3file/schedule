from app.domain.constants import NUMBERS_EMOJI
from app.domain.schemas import LessonOut


def build_schedule_day_text(day: str, lessons: list[LessonOut]) -> str:
    result = f"{day}\n\n"
    for lesson in lessons:
        result += f"{NUMBERS_EMOJI[lesson.time_window.id]}({lesson.lesson_type}) {lesson.name} ```{lesson.teacher.fullname}``` аудитория {lesson.audience} *{lesson.time_window.left_time_border}-{lesson.time_window.right_time_border}*\n\n"

    return result