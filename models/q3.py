# Existuje vazba valence (pozitivity/negativity) na období, která se vyznačují negativními událostmi (např. 2008, 2001)?
# V otázce je specifikováno období, hledáme tedy nějaký trend který se v čase drží, je tedy připuštěné i to, že bychom vybrali více než jeden rok.

import pandas as pd
import sys
from cleverminer.cleverminer import cleverminer
import matplotlib.pyplot as plt
import os
from histogram import draw_hist

# dataset_spotify_added.csv
df = pd.read_csv(
    sys.argv[1],
    usecols=["valence_cat", "spotify_release_date", "hit"],
    dtype={
        "valence_cat": "category",
        "spotify_release_date": "object",
        "hit": "int64"
    }
)

### 1. Existuje vazba nízké valence (převažující průměrné nebo podprůměrné) na nějaká konkrétní časová období?

relevant_df = df
relevant_df["year"] = "?"
print(relevant_df['valence_cat'])
categories = (list(relevant_df['valence_cat'].value_counts(sort = False).index))

for index, row in relevant_df.iterrows():
    date = row["spotify_release_date"]

    if "-" in date:
        date = str(date).split("-")[0]

    relevant_df.at[index, "year"] = date

hypo = cleverminer(
    df = relevant_df,
    target = 'valence_cat',
    proc = 'CFMiner',
    quantifiers = {'S_Down':4, 'Base': 500}, # valence_cat má 5 hodnot, base je zvolena tak, aby pokryla alespoň 1% skladeb v celém datasetu
    cond = {
        'attributes': [
            {'name': 'year', 'type': 'seq', 'minlen': 1, 'maxlen': 3}, # časové období které může být relevantní je těžké určit, ale musí být sekvenční. recese běžně trvají spíše 2 až 3 roky, politické krize spíše méně než rok, ve sledovaném období nebyl na relevantních trzích žádný dlouhodobý konflikt, tak kompromis 2-3 je asi v pořádku.
            {'name': 'hit', 'type': 'subset', 'minlen': 1, 'maxlen': 1} # 
        ],
        'minlen':1,
        'maxlen':2,
        'type':'con'
    }
)

res = hypo.result
current_dir = os.path.dirname(__file__)

for hypo in res["hypotheses"]:
    print(hypo["cedents"]["cond"] + ": " + str(hypo["params"]["base"]))
    print(hypo["params"]["hist"])

    draw_hist(
        os.path.join(current_dir, "q3", "histograms", hypo["cedents"]["cond"] + ".png"),
        "Cond:" + hypo["cedents"]["cond"] + ", base: " + str(hypo["params"]["base"]),
        hypo["params"]["hist"],
        categories,
        "Valence",
        "Count"
    )