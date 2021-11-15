import spotipy
import os
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
      client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
      client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET")
      #client_id='8fa7fd8c937847b8a85a549155713d01',
      #client_secret='301e22bcd4764bef877db63a8ca0c3e2'
    )
)

track = sp.track("spotify:track:6Rvlwah55rEmg1ufhBz022")
pprint(track)