from aiohttp import web

from app.core import views


def setup_routes(app: web.Application) -> None:
    app.router.add_get('/', views.index, name='index')
