from aiogram import Dispatcher


from app.api.handlers.user_handlers import router as main_router


async def include_routers(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(main_router)
