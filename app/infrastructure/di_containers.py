from dependency_injector import containers, providers

from app.injectors.group_injectors import get_group_service
from app.injectors.user_injectors import get_user_service


class ServiceContainer(containers.DeclarativeContainer):
    user_service = providers.Factory(
        get_user_service
    )
    group_service = providers.Factory(
        get_group_service
    )