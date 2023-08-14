"""`FactoryAggregate` provider with non-string keys example."""

from dependency_injector import containers, providers


# [TODO] Command
class Command:
    ...


# [TODO] CommandA
class CommandA(Command):
    ...


# [TODO] CommandB
class CommandB(Command):
    ...


# [TODO] Handler
class Handler:
    ...


# [TODO] HandlerA
class HandlerA(Handler):
    ...


# [TODO] HandlerB
class HandlerB(Handler):
    ...


# [TODO] Container
class Container(containers.DeclarativeContainer):

    handler_factory = providers.FactoryAggregate({
        CommandA: providers.Factory(HandlerA),
        CommandB: providers.Factory(HandlerB),
    })


if __name__ == "__main__":
    container = Container()

    handler_a = container.handler_factory(CommandA)
    handler_b = container.handler_factory(CommandB)

    assert isinstance(handler_a, HandlerA)
    assert isinstance(handler_b, HandlerB)