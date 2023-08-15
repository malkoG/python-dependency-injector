"""Message bus module."""

from typing import Dict, Callable, Any

from .commands import Command


# [TODO] MessageBus
class MessageBus:

    # [TODO] MessageBus > __init__
    def __init__(self, command_handlers: Dict[str, Callable[..., Any]]):
        self.command_handlers = command_handlers

    # [TODO] MessageBus > handle
    def handle(self, command: Command):
        self.command_handlers[command]()
