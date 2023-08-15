"""Wiring attribute example."""

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide


# [TODO] Service
class Service:
    ...


# [TODO] Container
class Container(containers.DeclarativeContainer):

    service = providers.Factory(Service)


service: Service = Provide[Container.service]


# [TODO] Main
class Main:

    service: Service = Provide[Container.service]


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    assert isinstance(service, Service)
    assert isinstance(Main.service, Service)
