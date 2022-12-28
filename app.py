import asyncio

from aiohttp import web

import settings
from __init__ import setup_app


def main() -> None:
    loop = asyncio.new_event_loop()

    app = web.Application()  # Создаем веб-сервер
    setup_app(app, settings)  # Настраиваем приложение

    web.run_app(app, loop=loop)  # Запускаем приложение


if __name__ == '__main__':
    main()
