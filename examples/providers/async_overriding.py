"""Provider overriding in async mode example."""

import asyncio

from dependency_injector import containers, providers


# [TODO] init_async_resource
async def init_async_resource():
    return ...


# [TODO] init_resource_mock
def init_resource_mock():
    return ...


# [TODO] Container
class Container(containers.DeclarativeContainer):

    resource = providers.Resource(init_async_resource)


# [TODO] main
async def main(container: Container):
    resource1 = await container.resource()

    container.resource.override(providers.Callable(init_resource_mock))
    resource2 = await container.resource()
    ...


if __name__ == "__main__":
    container = Container()

    asyncio.run(main(container))
