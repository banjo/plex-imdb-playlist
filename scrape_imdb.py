import requests
from bs4 import BeautifulSoup
from add_to_plex import add_playlist
import sys

""" scrape a custom made imdb list

if used in terminal, pass the following three arguments:
    * website url
    * playlist name
    * type ("movie" or "show")

"""
URL_PAGE = "?&mode=detail&page="
HEADERS = {"Accept-Language": "en-US,en;q=0.5"}


def scrape(website, playlist_name):
    """
    * website = url
    * playlist_name = name of playlist
    * type = 'movie' or 'show'
    """

    # create lists that takes all data from every loop
    movie_final = []
    year_final = []

    k = 1
    while True:

        print("Scraping page: " + str(k))

        html = requests.get(website + URL_PAGE + str(k), headers=HEADERS)
        soup = BeautifulSoup(html.content, "lxml")

        # find popular movies and years, and convert to list
        movies = soup.select(
            '#main > div > div.lister.list.detail.sub-list > div.lister-list > div > div.lister-item-content > h3 > a')
        years = soup.select(
            "#main > div > div.lister.list.detail.sub-list > div.lister-list > div > div.lister-item-content > h3 > span.lister-item-year.text-muted.unbold"
        )

        # break if there are not movies left
        if len(movies) == 0:
            break

        # get all movie titles and years
        movies_string = [movie.get_text() for movie in movies]
        years_int = [year.get_text().replace("(", "") for year in years]
        years_int = [year.replace(")", "") for year in years_int]
        years_int = [year.replace("I ", "") for year in years_int]

        # append all movies that are scraped
        movie_final = movie_final + movies_string.copy()
        year_final = year_final + years_int.copy()

        # loop
        k += 1

    # create dict for each movie
    movie_list = {}
    for i, movie in enumerate(movie_final):
        movie_list[movie] = {"title": movie, "year": year_final[i]}

    # add playlist to plex
    add_playlist(movie_list, playlist_name)


if __name__ == "__main__":
    scrape(sys.argv[1], sys.argv[2], sys.argv[3])
