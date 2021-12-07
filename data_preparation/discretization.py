import os
from numpy import row_stack
import pandas as pd
import sys
import matplotlib.pyplot as plt

dirname = os.path.dirname(__file__)

# print(sys.argv[1])

outpath = os.path.join(dirname, '..' + os.sep + 'output_data' + os.sep, "dataset_categorised_2.csv")
outpath_barcharts = os.path.join(dirname, '..' + os.sep + 'output_data' + os.sep, "barchartsCategorised")

frame = pd.read_csv("./output_data/dataset_merged_with_eras.csv")

def discretize_linear(df, column, bins):
    df[column + "_cat"] = pd.cut(df[column], bins, include_lowest=True)

# kvantily
discretize_linear(frame, "sections", [0, 8, 10, 12, 169])

# hodnoty jsou i přesto dost nesmyslné - asi ta heuristika co využil autor nebyla správně?
# myšlenka tu je nějak relativizovat tuhle hodnotu, protože v absolutních číslech nedává smysl ji "srovnávat"
frame["chorus_hit_pct"] = (frame["chorus_hit"] / frame["duration_ms"]) * 100

discretize_linear(frame, "chorus_hit_pct", 5)

# tady nevím - je to pořád hodně nevyvážené a nevím jak tu hodnotu interpretovat na udání taktu - většina je 4 a 3/4 je nejčastější, tak to spolu asi nějak souvisí - obecně by to šlo rozdělit na "konvenční a nekonvenční"
discretize_linear(frame, "time_signature", [0, 3.99, 4])

# v Pandas se to pak neformátuje ve vědecké notaci - tj. je to jednodušší přečíst
# oříznuto zleva - nejmenší interval
frame["duration_s"] = frame["duration_ms"] / 1000
discretize_linear(frame, "duration_s", [60, 120, 180, 240, 300, 1000])

# https://cs.wikipedia.org/wiki/Beats_per_minute
# tady jsem to ořezala o krajní intervaly
discretize_linear(frame, "tempo", [66, 76, 108, 120, 168, 208])

# 0.6 and greater indicate solid chances the track was performed live, anything nearing 1 was very likely performed live, between 0.4 and 0.6 it's basically "half", anything below that is certainly a studio recording
discretize_linear(frame, "liveness", [0, 0.4, 0.6, 0.8, 1])

# hodnota -1 je ve skutecnosti 0
discretize_linear(frame, "instrumentalness", [-1, 0, 0.1, 0.4, 0.7, 0.9, 1])

# Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks. 
discretize_linear(frame, "speechiness", [0, 0.33, 0.66, 1])
discretize_linear(frame, "loudness", [-100, -13, -9, -6, 4])

# Tyto atributy nabývají hodnot od 0.0 do 1.0 a dává smysl je rozdělit ekvidistančně na 5 intervalů
discretize_linear_0_1_ed = ["acousticness", "danceability", "energy", "valence", ]

# Key is already discrete - tóninu nedává smysl dále diskretizovat
discretize_linear(frame, "key", 12)

# Úprava hranic intervalů - automatické rozdělení do 5 binů generuje nečitelné hodnoty
for column in discretize_linear_0_1_ed:
    discretize_linear(frame, column, [0, 0.2, 0.4, 0.6, 0.8, 1])

print(frame.describe())
print(frame)

for (column, type) in frame.dtypes.iteritems():
    
    if ("_cat" not in column):
        continue

# přejmenování kategorií tónin (keys)
    if column == 'key_cat':
        labels = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        frame[column].cat.categories = labels
        #ax.set_xticklabels(labels)

# přejmenování krajního spodního intervalu - reálně neobsahuje záporné hodnoty, pouze 0
    if column == 'instrumentalness_cat':
        labels = frame[column].cat.categories.tolist()
        labels[0] = 0.0
        frame[column].cat.categories = labels
    
    print(frame[column])
    cats = frame[column].cat.categories.tolist()

    #plt.title(column)

    facecolor = '#EAEAEA'
    color_bars = '#3475D0'
    txt_color1 = '#252525'
    txt_color2 = '#004C74'

    fig, ax = plt.subplots(1)
    ax.set_facecolor(facecolor)

    frame[column].value_counts()[cats].plot(kind='bar')

    #frame[column].plot(kind='bar') #, dpi=199, rot=0, figsize=(10,6)

    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.xticks(c=txt_color1, fontsize=10, rotation=0)
    #if column == 'valence_cat':
        #plt.xticks(rotation=30)
    #if column == 'acousticness_cat':
        #plt.xticks(rotation=15)
    plt.yticks(c=txt_color1, fontsize=10)
    plt.title(column, loc = 'center', fontsize = 15, c=txt_color1)

    plt.grid(axis='y', color=color_bars, lw = 0.5, alpha=0.7)

    plt.tight_layout()
    plt.savefig(os.path.join(outpath_barcharts, column + ".png"), facecolor = facecolor)
    plt.close()

frame.to_csv(outpath, index=False)