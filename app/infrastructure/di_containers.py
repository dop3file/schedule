from dependency_injector import containers, providers

from app.injectors.user_injectors import get_user_service


class ServiceContainer(containers.DeclarativeContainer):
    user_service = providers.Factory(
        get_user_service
    )