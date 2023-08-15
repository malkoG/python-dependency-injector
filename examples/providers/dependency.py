"""`Dependency` provider example."""

import abc
import dataclasses

from dependency_injector import containers, providers


# [TODO] DbAdapter
class DbAdapter(metaclass=abc.ABCMeta):
    ...


# [TODO] SqliteDbAdapter
class SqliteDbAdapter(DbAdapter):
    ...


# [TODO] PostgresDbAdapter
class PostgresDbAdapter(DbAdapter):
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
    container1 = Container(database=providers.Singleton(SqliteDbAdapter))
    container2 = Container(database=providers.Singleton(PostgresDbAdapter))

    assert isinstance(container1.user_service().database, SqliteDbAdapter)
    assert isinstance(container2.user_service().database, PostgresDbAdapter)

    container3 = Container(database=providers.Singleton(object))
    container3.user_service()  # <-- raises error:
    # <object ...> is not an instance of DbAdapter
