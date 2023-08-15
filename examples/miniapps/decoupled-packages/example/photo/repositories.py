"""Photo repositories module."""


# [TODO] PhotoRepository
class PhotoRepository:

    # [TODO] PhotoRepository > __init__
    def __init__(self, entity_factory, fs, db):
        self.entity_factory = entity_factory
        self.fs = fs
        self.db = db

    # [TODO] PhotoRepository > get_photos
    def get_photos(self, user_id):
        return [self.entity_factory() for _ in range(user_id*5)]
