from operator import xor
import pandas as pd
import sys
import matplotlib.pyplot as plt
import os

dirname = os.path.dirname(__file__)

print(sys.argv[1])

frame = pd.read_csv(sys.argv[1])

discretize_columns = ["danceability", "energy", "key", "loudness", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo", "duration_ms", "time_signature", "chorus_hit", "sections"]

for column in discretize_columns:
    colname = column + "_q"
    df = frame[column]

    hist = df.hist(bins=5)
    plt.savefig(os.path.join(dirname, "out", "histograms", colname + ".png"), dpi=199)
    plt.close()