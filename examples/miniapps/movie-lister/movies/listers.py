"""Movie listers module."""

from .finders import MovieFinder


# [TODO] MovieLister
class MovieLister:

    # [TODO] MovieLister > __init__
    def __init__(self, movie_finder: MovieFinder):
        self._movie_finder = movie_finder

    # [TODO] MovieLister > movies_directed_by
    def movies_directed_by(self, director):
        return [
            movie for movie in self._movie_finder.find_all()
            if movie.director == director
        ]

    # [TODO] MovieLister > movies_released_in
    def movies_released_in(self, year):
        return [
            movie for movie in self._movie_finder.find_all()
            if movie.year == year
        ]