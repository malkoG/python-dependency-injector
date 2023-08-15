"""Use cases module."""

import abc

from .adapters import EmailSender


# [TODO] UseCase
class UseCase(metaclass=abc.ABCMeta):

    # [TODO] UseCase > execute
    @abc.abstractmethod
    def execute(self) -> None:
        ...


# [TODO] SignupUseCase
class SignupUseCase:

    # [TODO] SignupUseCase > __init__
    def __init__(self, email_sender: EmailSender) -> None:
        self.email_sender = email_sender

    # [TODO] SignupUseCase > execute
    def execute(self, email: str) -> None:
        print(f"Sign up user {email}")
        self.email_sender.send(email, f"Welcome, {email}")
