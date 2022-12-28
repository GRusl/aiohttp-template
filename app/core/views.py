from aiohttp import web


async def index(request: web.Request) -> web.Response:
    text = 'Hello, World!'
    return web.Response(text=text)
