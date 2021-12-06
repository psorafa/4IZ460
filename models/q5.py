import pandas as pd
import sys
from cleverminer.cleverminer import cleverminer
import matplotlib.pyplot as plt
import os
import numpy as np
from hypothesis import HypothesisWraper
from hypothesis import draw_fourfolds_best_confidence
from hypothesis import draw_fourfolds_best_base

#,track,artist,uri,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature,chorus_hit,sections,hit,era,sections_cat,chorus_hit_pct,chorus_hit_pct_cat,time_signature_cat,duration_s,duration_s_cat,tempo_cat,
# ,,,loudness_cat,acousticness_cat,danceability_cat,energy_cat,key_cat,valence_cat,spotify_explicit,spotify_track_number,spotify_release_date,spotify_disc_number,spotify_album_total_tracks,spotify_album_type,spotify_album_uri,spotify_artist_count,spotify_track_type,spotify_num_markets

df = pd.read_csv(
    "./output_data/dataset_categorised_2.csv",
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

for index in range(len(res["hypotheses"])):
    hypo = res["hypotheses"][index]
    base = hypo["params"]["base"]
    pim = hypo["params"]["pim"]
    all_hypotheses.append(
        HypothesisWraper(
            "q5",
            "4ft",
            hypo
        )
    )

draw_fourfolds_best_confidence(all_hypotheses, 10)

print("----------------")

draw_fourfolds_best_base(all_hypotheses, 10)