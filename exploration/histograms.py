import pandas as pd
import sys
import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns

dirname = os.path.dirname(__file__)
print(sys.argv[1])

frame = pd.read_csv(sys.argv[1])

fig, ax = plt.subplots(5,3, figsize=(20,20))

palette = sns.color_palette("cool", 15)
palette_hex = palette.as_hex()

def hist_plot(row, column, variable, binsnum):
    ax[row, column].hist(frame[variable], bins = binsnum, color = palette_hex[row*3+column])
    ax[row, column].set_title(variable + ' histogram')

    
hist_plot(0, 0, 'danceability', 10)
hist_plot(0, 1, 'energy', 10)
hist_plot(0, 2, 'key', 10)
hist_plot(1,0, 'loudness', 10)
hist_plot(1,1, 'mode', 10)
hist_plot(1,2, 'speechiness', 10)
hist_plot(2,0, 'acousticness', 10)
hist_plot(2,1, 'instrumentalness', 10)
hist_plot(2,2, 'liveness', 10)
hist_plot(3,0, 'valence', 10)
hist_plot(3,1, 'tempo', 10)
hist_plot(3,2, 'duration_s', 50)
hist_plot(4,0, 'time_signature', 10)
hist_plot(4,1, 'chorus_hit', 10)
hist_plot(4,2, 'sections', 25)

plt.savefig(os.path.join(dirname, "out", "histogramsSeaborn", "histogramsSubplots.png"), dpi=199)
plt.close()
