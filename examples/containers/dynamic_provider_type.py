"""Dynamic container provider type restriction example."""

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


services = containers.DynamicContainer()
services.provider_type = ServiceProvider

services.user_service = ServiceProvider(UserService)
services.other_provider = providers.Factory(object)
