"""Adapters module."""

import abc


# [TODO] EmailSender
class EmailSender(metaclass=abc.ABCMeta):

    # [TODO] EmailSender > send
    @abc.abstractmethod
    def send(self, to: str, body: str) -> None:
        ...


# [TODO] SmtpEmailSender
class SmtpEmailSender:

    # [TODO] SmtpEmailSender > send
    def send(self, to: str, body: str) -> None:
        print(f"Sending an email to {to} over SMTP, body=\"{body}\"")


# [TODO] EchoEmailSender
class EchoEmailSender:

    # [TODO] EchoEmailSender > send
    def send(self, to: str, body: str) -> None:
        print(f"Fake sending an email to {to}, body=\"{body}\"")
