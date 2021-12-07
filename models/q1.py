import pandas as pd
import sys
from cleverminer.cleverminer import cleverminer
import matplotlib.pyplot as plt
import os
import numpy as np
from histogram import draw_hist

# Mají taneční skladby výrazně větší hitový potenciál?
# Mění se tento potenciál v závislosti na dekádě?

# print(sys.argv[1])
df = pd.read_csv ("./output_data/dataset_categorised_2.csv")

# jinak CFMiner předpřipraví sloupečky které jsou nominální, což trvá dlouho

relevant_df = df[
    ["danceability_cat", "era", "hit", ]
]

# kategorialni int a dichotomickou promennou to neumi poznat...

relevant_df['era'] = pd.Series(df['era'], dtype="string")
relevant_df['hit'] = pd.Series(df['hit'], dtype="string")

eras = [ "60", "70", "80", "90", "0", "10"]

relevant_df["era"] = pd.Categorical(relevant_df['era'], eras, ordered=True)

# TJ. Chceme zjistit, zda skladby, které mají vysokou danceability_cat (right cuts - 2) nemají stejné histogramy
# pro stejná období.
# Jde to poznat z grafu kde je porovnáme vedle sebe.

hypo = cleverminer(
    df = relevant_df,
    target = 'era',
    proc = 'CFMiner',
    quantifiers = {'Base':50},
    cond = {
        'attributes': [
            {'name': 'danceability_cat', 'type': 'rcut', 'minlen': 2, 'maxlen': 2},
            {'name': 'hit', 'type': 'subset', 'minlen': 1, 'maxlen': 1}
        ],
        'minlen':2, # minlen 2 tady nenašlo žádnou hypotézu - tak nevim kde je chyba
        'maxlen':2,
        'type':'con'
    }
)

res = hypo.result
#print(res.taskinfo)

hist = []
titles = []

current_dir = os.path.dirname(__file__)

for hypo in res["hypotheses"]:

    print(hypo["cedents"])
    print(hypo["params"])
    print(hypo["cedents"]["cond"])
    print(hypo["params"]["hist"])

    hist.append(hypo["params"]["hist"])
    titles.append(hypo["cedents"]["cond"])

    draw_hist(
        os.path.join(current_dir, "q1", "histograms", hypo["cedents"]["cond"] + ".png"),
        hypo["cedents"]["cond"],
        hypo["params"]["hist"],
        eras,
        "Eras",
        "# Of tracks"
    )

    # když target je hit - první pozice v hist - 0, druhá - 1
    # když ne, tak to vypadá, že to respektuje to pořadí kategorií, co jsem specifikoval

# pozor, tohle funguje jen když jsou dvě možnosti

ind = np.arange(len(hist[0]))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, hist[0], width, label=titles[0])
rects2 = ax.bar(ind + width/2, hist[1], width, label=titles[1])

ax.legend(
    bbox_to_anchor=(1.1, 1.05)
)

eras.insert(0,0)
ax.set_xticklabels(eras)

plt.xlabel('Eras')
plt.ylabel('# Of tracks')
plt.title('Mají taneční skladby výrazně větší hitový potenciál?')

plt.legend(loc='best')
plt.savefig(os.path.join(current_dir, "q1", "histograms", "side-by-side.png"))

