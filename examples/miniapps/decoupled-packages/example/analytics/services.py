"""Analytics services module."""


# [TODO] AggregationService
class AggregationService:

    # [TODO] AggregationService > __init__
    def __init__(self, user_repository, photo_repository):
        self.user_repository = user_repository
        self.photo_repository = photo_repository