import jinja2
import aiohttp_jinja2

from aiohttp import web


def setup_routes(app: web.Application, settings) -> None:
    """
    In this function, url paths are configured for the entire application
    :param app: Application Object;
    :param settings: List of application names;
    :return: None;
    """
    app.router.add_static(settings.static_url, path=settings.static_path, name='static')
    for app_name in settings.apps:
        i = __import__(f'app.{app_name}.routes', fromlist=[''])
        i.setup_routes(app)


def setup_external_libraries(app: web.Application, templates_path: str) -> None:
    # Setting up jinja2
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
    setup_external_libraries(app, settings.template_path)  # External Library Settings
    setup_routes(app, settings)  # Application Router Settings
