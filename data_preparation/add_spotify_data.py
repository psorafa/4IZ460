import os
import pandas as pd
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET")
        #client_id='8fa7fd8c937847b8a85a549155713d01',
        #client_secret='301e22bcd4764bef877db63a8ca0c3e2'
    )
)

dirname = os.path.dirname(__file__)

print(sys.argv[1])

outpath = os.path.join(dirname, '..' + os.sep + 'output_data' + os.sep, "dataset_spotify_added.csv")

frame = pd.read_csv(sys.argv[1])

frame["spotify_explicit"] = "?"
frame["spotify_track_number"] = "?"
frame["spotify_release_date"] = "?"
frame["spotify_disc_number"] = "?"
frame["spotify_album_total_tracks"] = "?"
frame["spotify_album_type"] = "?"
frame["spotify_album_uri"] = "?"
frame["spotify_artist_count"] = "?"
frame["spotify_track_type"] = "?"
frame["spotify_num_markets"] = "?"

for index, row in frame.iterrows():
    if index > 0 and index % 10 == 0:
        frame.to_csv(outpath) # pro jistotu - cokoliv nečekaného...
        time.sleep(0.05)

    track = sp.track(row["uri"])


    frame.at[index, "spotify_explicit"] = track["explicit"]
    frame.at[index, "spotify_track_number"] = track["track_number"]
    frame.at[index, "spotify_track_type"] = track["type"]

    frame.at[index, "spotify_release_date"] = track["album"]["release_date"]
    frame.at[index, "spotify_disc_number"] = "disc_number"
    frame.at[index, "spotify_album_total_tracks"] = track["album"]["total_tracks"]
    frame.at[index, "spotify_album_type"] = track["album"]["album_type"]
    frame.at[index, "spotify_album_uri"] = track["album"]["uri"]
    frame.at[index, "spotify_artist_count"] = len(track["artists"])
    frame.at[index, "spotify_num_markets"] = len(track["available_markets"])

    print(index)

frame.to_csv(outpath)