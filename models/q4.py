import pandas as pd
import sys
from cleverminer.cleverminer import cleverminer
import matplotlib.pyplot as plt
import numpy as np
from hypothesis import HypothesisWraper
from hypothesis import draw_fourfolds_best_confidence
from hypothesis import draw_fourfolds_best_base

#,track,artist,uri,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature,chorus_hit,sections,hit,era,sections_cat,chorus_hit_pct,chorus_hit_pct_cat,time_signature_cat,duration_s,duration_s_cat,tempo_cat,
# ,,,loudness_cat,acousticness_cat,danceability_cat,energy_cat,key_cat,valence_cat,spotify_explicit,spotify_track_number,spotify_release_date,spotify_disc_number,spotify_album_total_tracks,spotify_album_type,spotify_album_uri,spotify_artist_count,spotify_track_type,spotify_num_markets

df = pd.read_csv(
    "./output_data/dataset_categorised_2.csv",
    usecols=["key_cat", "hit"],
    dtype={
        "key_cat": "category",
        "hit": "int64"
    }
)
# Existuje konkrétní tónina/skupina tónin, která výrazně převažuje mezi hity?
# Hledáme tedy vztah mezi kombinacemi hodnot tóniny a zda se stala skladba hitem či ne.

hypo = cleverminer(
    df=df,
    proc='4ftMiner',
    quantifiers= {'Base':1000, 'pim': 0.55}, 
    ante ={
        'attributes':[
            {'name': 'key_cat', 'type': 'subset', 'minlen': 1, 'maxlen': 5}
        ],
        'minlen':1,
        'maxlen':5,
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
all_hypotheses = []

for index in range(len(res["hypotheses"])):
    hypo = res["hypotheses"][index]
    base = hypo["params"]["base"]
    pim = hypo["params"]["pim"]
    all_hypotheses.append(
        HypothesisWraper(
            "q4",
            "4ft",
            hypo
        )
    )

draw_fourfolds_best_confidence(all_hypotheses, 10)

print("----------------")

draw_fourfolds_best_base(all_hypotheses, 10)