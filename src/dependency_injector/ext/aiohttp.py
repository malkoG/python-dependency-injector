"""Aiohttp extension module."""

from __future__ import absolute_import

import functools
import warnings

from dependency_injector import providers


warnings.warn(
    'Module "dependency_injector.ext.aiohttp" is deprecated since '
    'version 4.0.0. Use "dependency_injector.wiring" module instead.',
    category=DeprecationWarning,
)


# [TODO] Application
class Application(providers.Singleton):
    """Aiohttp application provider."""


# [TODO] Extension
class Extension(providers.Singleton):
    """Aiohttp extension provider."""


# [TODO] Middleware
class Middleware(providers.DelegatedCallable):
    """Aiohttp middleware provider."""

    __middleware_version__ = 1


# [TODO] MiddlewareFactory
class MiddlewareFactory(providers.Factory):
    """Aiohttp middleware factory provider."""


# [TODO] View
class View(providers.Callable):
    """Aiohttp view provider."""

    # [TODO] View > as_view
    def as_view(self):
        """Return aiohttp view function."""
        @functools.wraps(self.provides)
        async def _view(request, *args, **kwargs):
            return await self.__call__(request, *args, **kwargs)
        return _view


# [TODO] ClassBasedView
class ClassBasedView(providers.Factory):
    """Aiohttp class-based view provider."""

    # [TODO] ClassBasedView > as_view
    def as_view(self):
        """Return aiohttp view function."""
        async def _view(request, *args, **kwargs):
            return await self.__call__(request, *args, **kwargs)
        return _view
