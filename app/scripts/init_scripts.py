from app.domain.constants import DAYS, TIME_WINDOWS
from app.domain.schemas import DayIn, TimeWindow
from app.services.lesson_service import DayService, LessonService


async def insert_days(day_service: DayService) -> None:
    for idx, day in enumerate(DAYS):
        await day_service.create(
            DayIn(
                id=idx,
                name=day
            )
        )


async def insert_time_windows(lesson_service: LessonService) -> None:
    for idx, time_borders in TIME_WINDOWS.items():
        await lesson_service.create_time_window(
            TimeWindow(
                id=idx,
                left_time_border=time_borders.left_time_border,
                right_time_border=time_borders.right_time_border
            )
        )

