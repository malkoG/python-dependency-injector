"""`Dependency` provider undefined error example."""

import abc
import dataclasses

from dependency_injector import containers, providers


# [TODO] DbAdapter
class DbAdapter(metaclass=abc.ABCMeta):
    ...


# [TODO] UserService
@dataclasses.dataclass
class UserService:
    database: DbAdapter


# [TODO] Container
class Container(containers.DeclarativeContainer):

    database = providers.Dependency(instance_of=DbAdapter)

    user_service = providers.Factory(
        UserService,
        database=database,
    )


if __name__ == "__main__":
    container = Container()
    container.user_service()  # <-- raises error:
    # Dependency "Container.database" is not defined