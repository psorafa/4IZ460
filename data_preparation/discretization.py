import os
import pandas as pd
import sys

dirname = os.path.dirname(__file__)

print(sys.argv[1])

outpath = os.path.join(dirname, '..' + os.sep + 'output_data' + os.sep, "dataset_categorised.csv")

frame = pd.read_csv(sys.argv[1])

def discretize_linear(df, column, bins):
    df[column + "_cat"] = pd.cut(df[column], bins)

# kvantily
discretize_linear(frame, "sections", [0, 8, 10, 12, 169])

# hodnoty jsou i přesto dost nesmyslné - asi ta heuristika co využil autor nebyla správně?
# myšlenka tu je nějak relativizovat tuhle hodnotu, protože v absolutních číslech nedává smysl ji "srovnávat"
frame["chorus_hit_pct"] = (frame["chorus_hit"] / frame["duration_ms"]) * 100

discretize_linear(frame, "chorus_hit_pct", 5)

# tady nevím - je to pořád hodně nevyvážené a nevím jak tu hodnotu interpretovat na udání taktu - většina je 4 a 3/4 je nejčastější, tak to spolu asi nějak souvisí - obecně by to šlo rozdělit na "konvenční a nekonvenční"
discretize_linear(frame, "time_signature", [0, 3.99, 4])

# v Pandas se to pak neformátuje ve vědecké notaci - tj. je to jednodušší přečíst
frame["duration_s"] = frame["duration_ms"] / 1000
discretize_linear(frame, "duration_s", [0, 60, 120, 180, 240, 300, 1000])

# https://cs.wikipedia.org/wiki/Beats_per_minute
discretize_linear(frame, "tempo", [0, 40, 60, 66, 76, 108, 120, 168, 208, 250])

# 0.6 and greater indicate solid chances the track was performed live, anything nearing 1 was very likely performed live, between 0.4 and 0.6 it's basically "half", anything below that is certainly a studio recording
discretize_linear(frame, "liveness", [0, 0.4, 0.6, 0.8, 1])

discretize_linear(frame, "instrumentalness", [-1, 0, 0.1, 0.4, 0.7, 0.9, 1])

# Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks. 
discretize_linear(frame, "speechiness", [0, 0.33, 0.66, 1])
discretize_linear(frame, "loudness", [-100, -13, -9, -6, 4])

discretize_linear_five_bins = ["acousticness", "danceability", "energy", "key", "valence", ]

for column in discretize_linear_five_bins:
    discretize_linear(frame, column, 5)

print(frame.describe())
print(frame)

frame.to_csv(outpath, index=False)