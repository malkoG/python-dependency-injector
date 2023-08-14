"""`Singleton` provider full resetting example."""

from dependency_injector import containers, providers


# [TODO] Database
class Database:
    ...


# [TODO] UserService
class UserService:
    # [TODO] UserService > __init__
    def __init__(self, db: Database):
        self.db = db


# [TODO] Container
class Container(containers.DeclarativeContainer):

    database = providers.Singleton(Database)

    user_service = providers.Singleton(UserService, db=database)


if __name__ == "__main__":
    container = Container()

    user_service1 = container.user_service()

    container.user_service.full_reset()

    user_service2 = container.user_service()
    assert user_service2 is not user_service1
    assert user_service2.db is not user_service1.db