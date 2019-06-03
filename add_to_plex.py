import sys

from plexapi.server import PlexServer

# Configure to your settings
BASE_URL = 'PLEX URL'
TOKEN = 'PLEX TOKEN'
PLEX_SECTION = "LIBRARY NAME"

# users that should be added in your friend list, use email adresses.
USERS = ["EMAIL",
         "ADRESSES"]

# Connect to plex server
plex = PlexServer(BASE_URL, TOKEN)
plex_movies = plex.library.section(PLEX_SECTION)


def add_playlist(name_list, name):
    """Add playlist to plex server

    Arguments:
        name_list {list} -- list with name of all movies that should be added.
        name {string} -- name of the playlist in plex
    """

    movie_list = []

    for loop, movie in enumerate(name_list):

        # create the movie dict item
        movie = name_list[movie]

        # print which movie
        print(f"{loop + 1}/{len(name_list)} {movie['title']}")

        # get movie if it exists
        temp = get_movie(movie)

        # loop if it can't find the movie
        if temp is False:
            print("--- Could not find movie")
            continue

        # add to list if it can find it
        movie_list.append(temp)

    # create playlist
    playlist = plex.createPlaylist(name, movie_list)

    # copy to users
    copy_to_users(playlist, USERS)

    print("Done")


def copy_to_users(playlist, users):
    for user in users:
        playlist.copyToUser(user)
        print(f"Copied to {user}")


def get_movie(movie):
    results = plex.search(movie["title"])

    # return movie if it exists
    for plex_movie in results:

        if plex_movie.type == "movie" and str(plex_movie.year) in str(movie["year"]):
            return plex_movie

    return False


if __name__ == "__main__":
    add_playlist(sys.argv[1], sys.argv[2])
