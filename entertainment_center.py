"""Build media objects and use them to construct the movies page."""
from bs4 import BeautifulSoup as Soup
from fresh_tomatoes import open_movies_page
from media import Movie
import requests

URL_ROOT = 'http://www.imdb.com'


def retrieve_movies():
    """Scrape IMDB and retrieve information on top movies."""
    response = requests.get("http://www.imdb.com/chart/top?ref_=nv_mv_250_6")
    html = Soup(response.text, 'html.parser')
    title_tags = html.find_all('td', {'class': 'titleColumn'})
    movies = []
    for tag in title_tags[:25]:
        single_page = URL_ROOT + tag.find('a').attrs['href']
        movies.append(build_movie(single_page))
    return movies


def build_movie(movie_url):
    """Build movie object from movie URL page."""
    response = requests.get(movie_url)
    html = Soup(response.text, 'html.parser')
    title_tag = html.find('h1', {'itemprop': 'name'})
    title, year = title_tag.text.strip().split('\xa0')
    year = year[1:-1]
    duration = html.find('time', {'itemprop': 'duration'}).text.strip()
    duration_minutes = calculate_mins(duration)
    rating = html.find('span', {'itemprop': 'ratingValue'}).text
    mpaa_rating = html.find(
        'meta',
        {'itemprop': 'contentRating'}
    ).attrs['content']
    if mpaa_rating.upper() not in Movie.MPAA_RATINGS:
        mpaa_rating = ''
    poster_url = html.find(
        'div',
        {'class': 'poster'}
    ).find('img').attrs['src']
    synopsis = html.find('div', {'class': 'summary_text'}).text.strip()
    cast = html.find('table', {'class': 'cast_list'})
    cast_links = cast.find_all('td', {'itemprop': 'actor'})
    starring = [
        cast_links[0].text.strip(),
        cast_links[1].text.strip()
    ]
    trailer_tag = html.find('a', {'itemprop': 'trailer'})
    trailer_url = trailer_tag.attrs['data-video'] if trailer_tag else ''

    movie = Movie(
        title, synopsis, rating, poster_url, duration_minutes,
        starring, trailer_url, mpaa_rating, year
    )
    return movie


def calculate_mins(time_string):
    """Convert a time string into minutes."""
    hours, mins = time_string.split()
    hour_num = int(hours.replace('h', ''))
    min_num = int(mins.replace('min', ''))
    return hour_num * 60 + min_num

open_movies_page(retrieve_movies())
