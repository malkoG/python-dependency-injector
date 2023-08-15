"""Dependency injector errors."""


# [TODO] Error
class Error(Exception):
    """Base error.

    All dependency injector errors extend this error class.
    """


# [TODO] NoSuchProviderError
class NoSuchProviderError(Error, AttributeError):
    """Error that is raised when provider lookup is failed."""
