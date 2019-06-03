import sys

from scrape_imdb import scrape

# Add URL to a custom made IMDb list and the name you want the playlist to have.
IMDB_URL = "URL TO IMDB CUSTOM LIST"
PLAYLIST_TITLE = "TITLE OF PLAYLIST"

if __name__ == "__main__":
    scrape(IMDB_URL, PLAYLIST_TITLE)
