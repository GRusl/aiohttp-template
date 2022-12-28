import asyncio

from aiohttp import web

import settings
from setup_app import setup_app


def main() -> None:
    loop = asyncio.new_event_loop()

    app = web.Application()  # Creating a web server
    setup_app(app, settings)  # Setting up the application

    web.run_app(app, loop=loop)  # Launching the application


if __name__ == '__main__':
    main()
