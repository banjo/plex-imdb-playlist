# Create Plex Playlists Based on IMDb Lists

This is a script to create playlists on your Plex server based on custom made IMDb lists. 

## Usage
* Configure your plex settings at the top of `add_to_plex.py`.
  * `BASE_URL` = URL to Plex playlist
  * `TOKEN` = Your Plex token
  * `PLEX_SECTION` = Name of the library with all movies, often "Movies".
  * `USERS` = List of email adresses that should get the copy of the playlist.
* Configure the settings at the top of `plex_playlist.py`.
  * `IMDB_URL` = URL to custom IMDb list
  * `PLAYLIST_TITLE` = What you want your playlist to be named
* Run `plex_playlist.py`. 
  
## Information
* IMDb URL must be a custom made list. The URL often looks like this: `https://www.imdb.com/list/ls068082370/`
* It only works with movies, no TV shows.
* If the movie doesn't exist in the library, it just skips it. 
