"""Class descriptions for the media types handled by entertainment_center.py."""
import webbrowser


class Video(object):
    """Prototype object for movies and tv shows."""

    def __init__(self, title, synopsis, rating, poster_url):
        """Constructor for the Video object."""
        self.title = title
        self.synopsis = synopsis
        self.rating = rating
        self.poster_url = poster_url


class Movie(Video):
    """This class provides a way to store movie-related information."""

    MPAA_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, synopsis, poster_url, trailer_url, rating, mpaa_rating):
        """Constructor for the Movie object."""
        Video.__init__(self, title, synopsis, rating, poster_url)
        self.trailer_url = trailer_url
        self._validate_rating(mpaa_rating)

    def show_trailer(self):
        """Open the movie's trailer in the user's browser."""
        webbrowser.open(self.trailer_url)

    def _validate_rating(self, rating):
        """Check to make sure that the rating given is a valid MPAA rating."""
        if rating.upper() in self.MPAA_RATINGS:
            self.mpaa_rating = rating
        else:
            raise ValueError('This is not one of the valid MPAA ratings.')

    def __str__(self):
        """The string representation of the movie object."""
        return '<Movie | {} | {}>' .format(self.title, self.mpaa_rating)


class TVShow(Video):
    """This class provides a way to store tv-related information."""

    TV_CONTENT_RATINGS = ['Y', 'Y7', 'FV', 'G', 'PG', '14', 'MA']

    def __init__(self, title, synopsis, poster_url, rating, tv_rating):
        """Constructor for the TVShow object."""
        Video.__init__(self, title, synopsis, rating, poster_url)
        self._validate_rating(tv_rating)

    def _validate_rating(self, rating):
        """Check to make sure that the rating given is a valid TV content rating."""
        if rating.startswith('TV-') and rating[3:] in self.TV_CONTENT_RATINGS:
            self.tv_rating = rating
        else:
            raise ValueError('This is not one of the valid TV content ratings.')

    def __repr__(self):
        """The string representation of the tv show object."""
        return '<TV Show | {} | TV-{}>'.format(self.title, self.tv_rating)
