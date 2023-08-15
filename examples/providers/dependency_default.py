"""`Dependency` provider default example."""

import abc

from dependency_injector import containers, providers


# [TODO] Cache
class Cache(metaclass=abc.ABCMeta):
    ...


# [TODO] InMemoryCache
class InMemoryCache(Cache):
    ...


# [TODO] Container
class Container(containers.DeclarativeContainer):

    cache = providers.Dependency(instance_of=Cache, default=InMemoryCache())


if __name__ == "__main__":
    container = Container()
    cache = container.cache()  # provides InMemoryCache()

    assert isinstance(cache, InMemoryCache)
