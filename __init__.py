from aiohttp import web


def setup_routes(app: web.Application, apps: list[str]) -> None:
    for app_name in apps:
        i = __import__(f'app.{app_name}.routes', fromlist=[''])
        i.setup_routes(app)


def setup_app(app: web.Application, settings) -> None:
    # setup_external_libraries(app)  # Настройки внешних библиотек
    setup_routes(app, settings.apps)  # Настройки роутера приложения
