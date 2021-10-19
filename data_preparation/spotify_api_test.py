import spotipy
import os
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET")
    )
)

track = sp.track("spotify:track:6Rvlwah55rEmg1ufhBz022")
pprint(track)