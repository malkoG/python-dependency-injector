"""Handlers module."""

from .repositories import RatingRepository


# [TODO] CommandHandler
class CommandHandler:
    # [TODO] CommandHandler > __init__
    def __init__(self, rating_repo: RatingRepository):
        self.rating_repo = rating_repo

    # [TODO] CommandHandler > save_rating
    def save_rating(self):
        print("Saving rating")

    # [TODO] CommandHandler > something_else
    def something_else(self):
        print("Doing something else")