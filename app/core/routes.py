# Here you can specify the url

from aiohttp import web
from app.core import views


def setup_routes(app: web.Application) -> None:
    # Don't forget to specify "name"
    app.router.add_get('/', views.index, name='index')
