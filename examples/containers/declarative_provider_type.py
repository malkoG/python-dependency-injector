"""Declarative container provider type restriction example."""

import abc

from dependency_injector import containers, providers


# [TODO] Service
class Service(metaclass=abc.ABCMeta):
    ...


# [TODO] UserService
class UserService(Service):
    ...


# [TODO] ServiceProvider
class ServiceProvider(providers.Factory):

    provided_type = Service


# [TODO] ServiceContainer
class ServiceContainer(containers.DeclarativeContainer):

    provider_type = ServiceProvider


# [TODO] MyServices
class MyServices(ServiceContainer):

    user_service = ServiceProvider(UserService)


# [TODO] ImproperServices
class ImproperServices(ServiceContainer):

    other_provider = providers.Factory(object)
