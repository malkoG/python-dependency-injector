"""Asynchronous injections example."""

import asyncio

from dependency_injector import containers, providers


# [TODO] init_async_resource
async def init_async_resource():
    await asyncio.sleep(0.1)
    yield "Initialized"


# [TODO] Service
class Service:
    # [TODO] Service > __init__
    def __init__(self, resource):
        self.resource = resource


# [TODO] Container
class Container(containers.DeclarativeContainer):

    resource = providers.Resource(init_async_resource)

    service = providers.Factory(
        Service,
        resource=resource,
    )


# [TODO] main
async def main(container: Container):
    resource = await container.resource()
    service = await container.service()
    ...


if __name__ == "__main__":
    container = Container()

    asyncio.run(main(container))