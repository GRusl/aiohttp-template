import os

import jinja2
import aiohttp_jinja2

from aiohttp import web
from tortoise.contrib.aiohttp import register_tortoise


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


def setup_external_libraries(app: web.Application, settings) -> None:
    # Setting up jinja2
    aiohttp_jinja2.setup(
        app,
        enable_async=True,
        loader=jinja2.FileSystemLoader(settings.template_path),
        context_processors=[
            aiohttp_jinja2.request_processor
        ]
    )
    # Register tortoise-orm
    if any([os.path.exists(f'./app/{app_name}/models.py') for app_name in settings.apps]):
        # If there are models in the applications
        register_tortoise(
            app,
            db_url='sqlite://database.sqlite3',
            modules={
                app_name: [f'app.{app_name}.models']
                for app_name in settings.apps if os.path.exists(f'./app/{app_name}/models.py')
            },
            generate_schemas=True,
        )


def setup_app(app: web.Application, settings) -> None:
    setup_external_libraries(app, settings)  # External Library Settings
    setup_routes(app, settings)  # Application Router Settings
