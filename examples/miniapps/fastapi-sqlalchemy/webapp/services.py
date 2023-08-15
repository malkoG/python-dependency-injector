"""Services module."""

from uuid import uuid4
from typing import Iterator

from .repositories import UserRepository
from .models import User


# [TODO] UserService
class UserService:

    # [TODO] UserService > __init__
    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    # [TODO] UserService > get_users
    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    # [TODO] UserService > get_user_by_id
    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    # [TODO] UserService > create_user
    def create_user(self) -> User:
        uid = uuid4()
        return self._repository.add(email=f"{uid}@email.com", password="pwd")

    # [TODO] UserService > delete_user_by_id
    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)
