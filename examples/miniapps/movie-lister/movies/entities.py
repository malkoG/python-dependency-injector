"""Movie entities module."""


# [TODO] Movie
class Movie:

    # [TODO] Movie > __init__
    def __init__(self, title: str, year: int, director: str):
        self.title = str(title)
        self.year = int(year)
        self.director = str(director)

    # [TODO] Movie > __repr__
    def __repr__(self):
        return "{0}(title={1}, year={2}, director={3})".format(
            self.__class__.__name__,
            repr(self.title),
            repr(self.year),
            repr(self.director),
        )
