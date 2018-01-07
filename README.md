# The Python Movie Site

**Author**: Nicholas Hunt-Walker

**Description**: This site takes the top 25 movies from IMDB (http://www.imdb.com) and summarizes their data. If you click on the images, the trailer for those 25 movies shows up in a popup for you to play at your leisure.

## Getting Started

- Clone the repository to your computer

```
$ git clone https://github.com/nhuntwalker/movie-site.git
```

- Change directory into the cloned repository
- Start a Python virtual environment. Python 3.6+ is preferred, but the code should work in Python 2.7+ as well.

```
# With Python 3
$ python3 -m venv ENV
$ source ENV/bin/activate
(ENV) $

# With Python 2
$ pip install virtualenv
$ virtualenv ./ENV
$ source ENV/bin/activate
(ENV) $
```

- Install the packages in the `requirements.txt` file

```
(ENV) $ pip install -r requirements.txt
```

- Run the code with `python entertainment_center.py`
    + **NOTE**: When you run the code you may see the following error message: `0:100: execution error: "file:///path/to/code/fresh_tomatoes.html" doesn’t understand the “open location” message. (-1708)`. This is not of actual concern; the page will still open just fine.

## Dependencies

- [Requests](http://docs.python-requests.org/en/master/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)