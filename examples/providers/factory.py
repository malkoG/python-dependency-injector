"""`Factory` provider example."""

from dependency_injector import containers, providers


# [TODO] User
class User:
    ...


# [TODO] Container
class Container(containers.DeclarativeContainer):

    user_factory = providers.Factory(User)


if __name__ == "__main__":
    container = Container()

    user1 = container.user_factory()
    user2 = container.user_factory()
