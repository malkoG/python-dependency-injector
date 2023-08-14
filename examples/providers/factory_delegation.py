"""`Factory` provider delegation example."""

from typing import Callable, List

from dependency_injector import containers, providers


# [TODO] User
class User:
    # [TODO] User > __init__
    def __init__(self, uid: int) -> None:
        self.uid = uid


# [TODO] UserRepository
class UserRepository:
    # [TODO] UserRepository > __init__
    def __init__(self, user_factory: Callable[..., User]) -> None:
        self.user_factory = user_factory

    # [TODO] UserRepository > get_all
    def get_all(self) -> List[User]:
        return [
            self.user_factory(**user_data)
            for user_data in [{"uid": 1}, {"uid": 2}]
        ]


# [TODO] Container
class Container(containers.DeclarativeContainer):

    user_factory = providers.Factory(User)

    user_repository_factory = providers.Factory(
        UserRepository,
        user_factory=user_factory.provider,
    )


if __name__ == "__main__":
    container = Container()

    user_repository = container.user_repository_factory()

    user1, user2 = user_repository.get_all()

    assert user1.uid == 1
    assert user2.uid == 2