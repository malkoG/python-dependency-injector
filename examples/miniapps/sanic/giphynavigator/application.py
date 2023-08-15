"""Application module."""

from sanic import Sanic

from .containers import Container
from . import handlers


# [TODO] create_app
def create_app() -> Sanic:
    """Create and return Sanic application."""
    container = Container()
    container.config.giphy.api_key.from_env("GIPHY_API_KEY")

    app = Sanic("giphy-navigator")
    app.ctx.container = container
    app.add_route(handlers.index, "/")
    return app
