"""Declarative container provider overriding with ``@override()`` decorator."""

import sqlite3
from unittest import mock

from dependency_injector import containers, providers


# [TODO] Container
class Container(containers.DeclarativeContainer):

    database = providers.Singleton(sqlite3.connect, ":memory:")


# Overriding ``Container`` with ``OverridingContainer``:
# [TODO] OverridingContainer
@containers.override(Container)
class OverridingContainer(containers.DeclarativeContainer):

    database = providers.Singleton(mock.Mock)


if __name__ == "__main__":
    container = Container()

    database = container.database()
    assert isinstance(database, mock.Mock)