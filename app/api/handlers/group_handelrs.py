from aiogram import Router
from aiogram.types import CallbackQuery

from app.api.callback_datas import SelectGroupCallbackData, SelectSubGroupCallbackData
from app.api.filters import Text
from app.api.keyboards import get_subgroups_keyboard
from app.domain.constants import CHOOSE_GROUP_FINAL_TEXT, CHOOSE_SUBGROUP_TEXT
from app.domain.schemas import UserIn, Subgroups
from app.services.group_service import GroupService
from app.services.user_service import UserService


router = Router()


@router.callback_query(Text(startswith=SelectGroupCallbackData.callback_data.format("")))
async def choose_group(
    callback: CallbackQuery,
    user_in: UserIn,
    user_service: UserService,
    group_service: GroupService
):
    group_id = SelectGroupCallbackData.get_id_from_select_group_callback(callback.data)
    group = await group_service.get(group_id)
    all_subgroups = await group_service.get_all_subgroups(group.name)
    subgroups = Subgroups(
        subgroups=[group.subgroup for group in all_subgroups],
        ids=[group.id for group in all_subgroups]
    )
    await callback.message.answer(
        CHOOSE_SUBGROUP_TEXT,
        reply_markup=await get_subgroups_keyboard(subgroups)
    )


@router.callback_query(Text(startswith=SelectSubGroupCallbackData.callback_data.format("")))
async def choose_subgroup(
    callback: CallbackQuery,
    user_in: UserIn,
    user_service: UserService,
    group_service: GroupService
):
    group_id = SelectSubGroupCallbackData.get_id_from_select_group_callback(callback.data)
    await user_service.update_user_group(user_in, group_id)
    await callback.message.answer(
        CHOOSE_GROUP_FINAL_TEXT
    )