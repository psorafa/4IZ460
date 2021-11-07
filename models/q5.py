import pandas as pd
import sys
from cleverminer.cleverminer import cleverminer
import matplotlib.pyplot as plt
import os
import numpy as np
from table import draw_table

#,track,artist,uri,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature,chorus_hit,sections,hit,era,sections_cat,chorus_hit_pct,chorus_hit_pct_cat,time_signature_cat,duration_s,duration_s_cat,tempo_cat,
# ,,,loudness_cat,acousticness_cat,danceability_cat,energy_cat,key_cat,valence_cat,spotify_explicit,spotify_track_number,spotify_release_date,spotify_disc_number,spotify_album_total_tracks,spotify_album_type,spotify_album_uri,spotify_artist_count,spotify_track_type,spotify_num_markets

df = pd.read_csv(
    sys.argv[1],
    usecols=["liveness_cat", "instrumentalness_cat", "speechiness_cat", "hit"],
    dtype={
        "liveness_cat": "category",
        "instrumentalness_cat": "category",
        "speechiness_cat": "category",
        "hit": "int64"
    }
)
# Jak moc ovlivňuje instrumentálnost, přítomnost mluveného slova a způsob nahrávání skladeb jejich výslednou popularitu?
# Hledáme tedy vztah mezi těmito sloupečky a tím, zda se stala skladba hitem či ne.

hypo = cleverminer(
    df=df,
    proc='4ftMiner',
    quantifiers= {'Base':500}, # cca 1 % skladeb minimálně
    ante ={
        'attributes':[
            {'name': 'liveness_cat', 'type': 'seq', 'minlen': 1, 'maxlen': 2},
            {'name': 'instrumentalness_cat', 'type': 'seq', 'minlen': 1, 'maxlen': 2},
            {'name': 'speechiness_cat', 'type': 'subset', 'minlen': 1, 'maxlen': 1}
        ],
        'minlen':1, # zde mi jakákoliv vyšší úroveň minlen hodila chybu
        'maxlen':3,
        'type':'con'
    },
    succ ={
        'attributes':[
            {'name': 'hit', 'type': 'subset', 'minlen': 1, 'maxlen': 1}
        ],
        'minlen':1,
        'maxlen':1,
        'type':'con'
    },
)

res = hypo.result
current_dir = os.path.dirname(__file__)

all_hypotheses = []

class Hypothesis:
    
    def __init__(self, hypothesis, pim, base) -> None:
        self.hypothesis = hypothesis
        self.pim = pim
        self.base = base
        
    def draw_fourfold(self, filename_prepend = None) -> None:
        ant = self.hypothesis["cedents"]["ante"]
        suc = self.hypothesis["cedents"]["succ"]
        base = self.hypothesis["params"]["base"]
        pim = self.hypothesis["params"]["pim"]
        aa = self.hypothesis["params"]["aad"]

        filename = (str(filename_prepend) if filename_prepend != None else "") + ant + "_" + suc + ".png"

        draw_table(
            os.path.join(current_dir, "q5", "tables", filename),
            ant + "-> " + suc,
            ant,
            suc,
            self.hypothesis["params"]["fourfold"]
        )

for index in range(len(res["hypotheses"])):
    hypo = res["hypotheses"][index]
    base = hypo["params"]["base"]
    pim = hypo["params"]["pim"]
    all_hypotheses.append(
        Hypothesis(
            hypo,
            pim,
            base
        )
    )

# Vybereme pravidla s nejlepší podporou

best_pim = sorted(all_hypotheses, key = lambda x: x.pim, reverse=True)

num_hypo = 10

num_list = 0

for i in range(0, len(best_pim)):
    if best_pim[i].hypothesis["cedents"]["succ"] == "hit(0 )":
        #print(best_pim[i].hypothesis)

        best_pim[i].draw_fourfold(str(num_list) + "_" + "best_pim_hit_0_")

        num_list = num_list + 1
        
        if num_list > num_hypo:
            break

num_list = 0

for i in range(0, len(best_pim)):
    if best_pim[i].hypothesis["cedents"]["succ"] == "hit(1 )":
        #print(best_pim[i].hypothesis)

        best_pim[i].draw_fourfold(str(num_list) + "_" + "best_pim_hit_1_")

        num_list = num_list + 1
        
        if num_list > num_hypo:
            break


print("----------------")

num_list = 0

best_base = sorted(all_hypotheses, key = lambda x: x.base, reverse=True)

for i in range(0, len(best_base)):
    if best_base[i].hypothesis["cedents"]["succ"] == "hit(1 )":
        #print(best_base[i].hypothesis)

        best_base[i].draw_fourfold(str(num_list) + "_" + "best_base_")

        num_list = num_list + 1

        if num_list > num_hypo:
            break