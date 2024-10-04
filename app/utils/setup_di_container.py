from app.infrastructure.di_containers import ServiceContainer


def setup_di_containers() -> None:
    container = ServiceContainer()
    container.init_resources()
    container.wire(
        packages=[
            "api"
        ],
        modules=[
            "api.handlers.handlers",
            "api.middlewares"
        ]
    )