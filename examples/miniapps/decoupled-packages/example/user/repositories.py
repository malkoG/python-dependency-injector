"""User repositories module."""


# [TODO] UserRepository
class UserRepository:

    # [TODO] UserRepository > __init__
    def __init__(self, entity_factory, db):
        self.entity_factory = entity_factory
        self.db = db

    # [TODO] UserRepository > get
    def get(self, id):
        return self.entity_factory(id=id)