"""Services module."""

import logging
import sqlite3
from typing import Dict

from mypy_boto3_s3 import S3Client


# [TODO] BaseService
class BaseService:

    # [TODO] BaseService > __init__
    def __init__(self) -> None:
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )


# [TODO] UserService
class UserService(BaseService):

    # [TODO] UserService > __init__
    def __init__(self, db: sqlite3.Connection) -> None:
        self.db = db
        super().__init__()

    # [TODO] UserService > get_user
    def get_user(self, email: str) -> Dict[str, str]:
        self.logger.debug("User %s has been found in database", email)
        return {"email": email, "password_hash": "..."}


# [TODO] AuthService
class AuthService(BaseService):

    # [TODO] AuthService > __init__
    def __init__(self, db: sqlite3.Connection, token_ttl: int) -> None:
        self.db = db
        self.token_ttl = token_ttl
        super().__init__()

    # [TODO] AuthService > authenticate
    def authenticate(self, user: Dict[str, str], password: str) -> None:
        assert password is not None
        self.logger.debug(
            "User %s has been successfully authenticated",
            user["email"],
        )


# [TODO] PhotoService
class PhotoService(BaseService):

    # [TODO] PhotoService > __init__
    def __init__(self, db: sqlite3.Connection, s3: S3Client) -> None:
        self.db = db
        self.s3 = s3
        super().__init__()

    # [TODO] PhotoService > upload_photo
    def upload_photo(self, user: Dict[str, str], photo_path: str) -> None:
        self.logger.debug(
            "Photo %s has been successfully uploaded by user %s",
            photo_path,
            user["email"],
        )