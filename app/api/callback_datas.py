from dataclasses import dataclass


@dataclass
class SelectGroupCallbackData:
    callback_data: str = "select_group_{}"

    @staticmethod
    def get_id_from_select_group_callback(callback_data: str) -> int:
        return int(callback_data.split("_")[2])


@dataclass
class SelectSubGroupCallbackData:
    callback_data: str = "select_subgroup_{}"

    @staticmethod
    def get_id_from_select_group_callback(callback_data: str) -> int:
        return int(callback_data.split("_")[2])