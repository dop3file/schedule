from aiogram import Dispatcher


from app.api.handlers.user_handlers import router as user_router
from app.api.handlers.group_handelrs import router as group_router
from app.api.handlers.schedule_handlers import router as schedule_router


async def include_routers(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(user_router)
    dispatcher.include_router(group_router)
    dispatcher.include_router(schedule_router)