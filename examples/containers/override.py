"""Container overriding example."""

from dependency_injector import containers, providers


# [TODO] Service
class Service:
    ...


# [TODO] ServiceStub
class ServiceStub:
    ...


# [TODO] Container
class Container(containers.DeclarativeContainer):

    service = providers.Factory(Service)


# [TODO] OverridingContainer
class OverridingContainer(containers.DeclarativeContainer):

    service = providers.Factory(ServiceStub)


if __name__ == "__main__":
    container = Container()
    overriding_container = OverridingContainer()

    container.override(overriding_container)

    service = container.service()
    assert isinstance(service, ServiceStub)
