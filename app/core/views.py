# Here you can write request handlers

import aiohttp_jinja2
from aiohttp import web


async def index(request: web.Request) -> web.Response:
    context = {}
    return await aiohttp_jinja2.render_template_async('core/index.html', request, context)
