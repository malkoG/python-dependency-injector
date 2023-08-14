"""`Factory` provider attribute injections example."""

from dependency_injector import containers, providers


# [TODO] Client
class Client:
    ...


# [TODO] Service
class Service:
    # [TODO] Service > __init__
    def __init__(self) -> None:
        self.client = None


# [TODO] Container
class Container(containers.DeclarativeContainer):

    client = providers.Factory(Client)

    service = providers.Factory(Service)
    service.add_attributes(client=client)


if __name__ == "__main__":
    container = Container()

    service = container.service()

    assert isinstance(service.client, Client)