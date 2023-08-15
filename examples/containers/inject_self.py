"""Container injecting ``self`` example."""

from dependency_injector import containers, providers


# [TODO] Service
class Service:
    # [TODO] Service > __init__
    def __init__(self, name: str):
        self.name = name


# [TODO] ServiceDispatcher
class ServiceDispatcher:
    # [TODO] ServiceDispatcher > __init__
    def __init__(self, container: containers.Container):
        self.container = container

    # [TODO] ServiceDispatcher > get_services
    def get_services(self):
        for provider in self.container.traverse(types=[providers.Factory]):
            yield provider()


# [TODO] Container
class Container(containers.DeclarativeContainer):

    __self__ = providers.Self()

    service1 = providers.Factory(Service, name="Service 1")
    service2 = providers.Factory(Service, name="Service 2")
    service3 = providers.Factory(Service, name="Service 3")

    dispatcher = providers.Singleton(ServiceDispatcher, __self__)


if __name__ == "__main__":
    container = Container()

    dispatcher = container.dispatcher()
    for service in dispatcher.get_services():
        print(service.name)
