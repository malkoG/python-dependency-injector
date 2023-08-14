"""`Dict` provider with non-string keys example."""

import dataclasses
from typing import Dict

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


# [TODO] Dispatcher
@dataclasses.dataclass
class Dispatcher:
    command_handlers: Dict[Command, Handler]


# [TODO] Container
class Container(containers.DeclarativeContainer):

    dispatcher_factory = providers.Factory(
        Dispatcher,
        command_handlers=providers.Dict({
            CommandA: providers.Factory(HandlerA),
            CommandB: providers.Factory(HandlerB),
        }),
    )


if __name__ == "__main__":
    container = Container()

    dispatcher = container.dispatcher_factory()

    assert isinstance(dispatcher.command_handlers, dict)
    assert isinstance(dispatcher.command_handlers[CommandA], HandlerA)
    assert isinstance(dispatcher.command_handlers[CommandB], HandlerB)

    # Call "dispatcher = container.dispatcher_factory()" is equivalent to:
    # dispatcher = Dispatcher(
    #     command_handlers={
    #         CommandA: HandlerA(),
    #         CommandB: HandlerB(),
    #     },
    # )