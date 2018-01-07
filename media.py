"""Class descriptions for the media types handled by entertainment_center.py."""


class Video(object):
    """Prototype object for movies and tv shows."""

    def __init__(self, title, synopsis, rating, poster_url, duration, starring):
        """Constructor for the Video object."""
        self.title = title
        self.synopsis = synopsis
        self.rating = rating
        self.poster_url = poster_url
        self.duration = duration
        self.starring = starring


class Movie(Video):
    """This class provides a way to store movie-related information."""

    MPAA_RATINGS = ['G', 'PG', 'PG-13', 'R', '']

    def __init__(
        self, title, synopsis, rating, poster_url, duration,
        starring, trailer_id, mpaa_rating, year
    ):
        """Constructor for the Movie object."""
        Video.__init__(
            self, title, synopsis, rating, poster_url,
            duration, starring
        )
        self.trailer_id = trailer_id
        self.year = year
        self._validate_rating(mpaa_rating)

    def _validate_rating(self, rating):
        """Check the rating given is a valid MPAA rating."""
        if rating.upper() in self.MPAA_RATINGS:
            self.mpaa_rating = rating
        else:
            raise ValueError('This is not a valid MPAA rating.')

    def __repr__(self):
        """The string representation of the movie object."""
        return '<Movie | {} | {}>' .format(self.title, self.mpaa_rating)
