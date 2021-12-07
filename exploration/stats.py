import os
import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# print(sys.argv[1])

frame = pd.read_csv("./output_data/dataset_categorised_2.csv")

print(frame.describe())

features = ['track', 'artist', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 
                'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature', 
                'chorus_hit','sections', 'duration_s']

X = frame[features]

plt.figure(figsize=(15,6))
sns.heatmap(X.corr(),annot=True)
plt.title("Correlation Matrix")
# plt.show()

all_tracks_hits = frame[features].loc[frame['hit'] == 1]
all_tracks_flops = frame[features].loc[frame['hit'] == 0]
hits_means = pd.DataFrame(all_tracks_hits.describe().loc['mean'])
flops_means = pd.DataFrame(all_tracks_flops.describe().loc['mean'])
means_joined = pd.concat([hits_means,flops_means], axis = 1)
means_joined.columns = ['hit_mean', 'flop_mean']

print(means_joined)

# vypada to, ze atributy jako danceability, energy, loudness, instrumentalness, 
# acousticness, liveness, valence
# budou vic ovlivnovat cilovy atribut - ale nektere budou korelovane 

corr = frame[features].corr(method='pearson').abs()
# maska na dolni trojuhelnik matice - jinak jsou ve vysledku diagonaly (korelace=1) a duplicity 
corr = corr.mask(np.tril(np.ones(corr.shape)).astype(bool))
# filtr na korelaci vetsi nez 0.6
s = corr[corr > 0.6].stack().reset_index()
#sorted = s.sort_values(kind="quicksort", ascending=False)
# print(s)

originalCorr = frame[['energy','loudness','acousticness','sections','duration_s']].corr(method='pearson')
originalCorr.to_csv("corr.csv", index=True)
# print(originalCorr)
# takze ano podle predpokladu koreluji spolu pozitivne energy a loudness, sections a duration (ofc) - ty sections asi chceme vynechat stejne to je nesmysl
# a negativne koreluje energy a acousticness