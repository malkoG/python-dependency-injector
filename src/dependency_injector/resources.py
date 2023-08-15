"""Resources module."""

import abc
from typing import TypeVar, Generic, Optional


T = TypeVar("T")


# [TODO] Resource
class Resource(Generic[T], metaclass=abc.ABCMeta):

    # [TODO] Resource > init
    @abc.abstractmethod
    def init(self, *args, **kwargs) -> Optional[T]:
        ...

    # [TODO] Resource > shutdown
    def shutdown(self, resource: Optional[T]) -> None:
        ...


# [TODO] AsyncResource
class AsyncResource(Generic[T], metaclass=abc.ABCMeta):

    # [TODO] AsyncResource > init
    @abc.abstractmethod
    async def init(self, *args, **kwargs) -> Optional[T]:
        ...

    # [TODO] AsyncResource > shutdown
    async def shutdown(self, resource: Optional[T]) -> None:
        ...
