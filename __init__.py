import jinja2
import aiohttp_jinja2

from aiohttp import web


# В этой функции производится настройка url-путей для всего приложения
def setup_routes(app: web.Application, apps: list[str]) -> None:
    for app_name in apps:
        i = __import__(f'app.{app_name}.routes', fromlist=[''])
        i.setup_routes(app)


def setup_external_libraries(app: web.Application, templates_path: str) -> None:
    # Настраиваем шаблонизатор
    aiohttp_jinja2.setup(
        app,
        enable_async=True,
        loader=jinja2.FileSystemLoader(templates_path),
        context_processors=[
            # user_ctx_processor,
            aiohttp_jinja2.request_processor
        ]
    )
    # Настройка tortoise
    # register_tortoise(
    #     app,
    #     db_url='sqlite://main.sqlite3',
    #     modules={
    #         'abbreviator': ['app.abbreviator.models'],
    #         'users': ['app.users.models'],
    #     },
    #     generate_schemas=True,
    # )


def setup_app(app: web.Application, settings) -> None:
    setup_external_libraries(app, settings.templates_path)  # Настройки внешних библиотек
    setup_routes(app, settings.apps)  # Настройки роутера приложения
