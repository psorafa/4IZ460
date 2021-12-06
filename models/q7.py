import pandas as pd
import sys
from cleverminer.cleverminer import cleverminer
import matplotlib.pyplot as plt
import os
import numpy as np
from hypothesis import HypothesisWraper
from hypothesis import draw_double_fourfolds_greatest_deltapim

#,track,artist,uri,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature,chorus_hit,sections,hit,era,sections_cat,chorus_hit_pct,chorus_hit_pct_cat,time_signature_cat,duration_s,duration_s_cat,tempo_cat,
# ,,,loudness_cat,acousticness_cat,danceability_cat,energy_cat,key_cat,valence_cat,spotify_explicit,spotify_track_number,spotify_release_date,spotify_disc_number,spotify_album_total_tracks,spotify_album_type,spotify_album_uri,spotify_artist_count,spotify_track_type,spotify_num_markets

df = pd.read_csv(
    "./output_data/dataset_categorised_2.csv",
    usecols=["danceability_cat", "instrumentalness_cat", "acousticness_cat", "duration_s_cat", "hit"],
    dtype={
        "danceability_cat": "category",
        "instrumentalness_cat": "category",
        "acousticness_cat": "category",
        "duration_s_cat": "category",
        "hit": "int64"
    }
)

hypo = cleverminer(df=df,proc='SD4ftMiner',
    quantifiers= {'Base1':100, 'Base2':100, 'Deltapim' : 0.55},
    ante ={
         'attributes':[
            {'name': 'danceability_cat', 'type': 'seq', 'minlen': 1, 'maxlen': 3},
            {'name': 'instrumentalness_cat', 'type': 'seq', 'minlen': 1, 'maxlen': 3},
            {'name': 'acousticness_cat', 'type': 'seq', 'minlen': 1, 'maxlen': 3}
        ],
        'minlen':1,
        'maxlen':3,
        'type':'con'
        },
    succ ={
        'attributes':[
            {'name': 'hit', 'type': 'subset', 'minlen': 1, 'maxlen': 1}
        ], 'minlen':1, 'maxlen':1, 'type':'con'},
    frst ={
        'attributes':[
            {'name': 'duration_s_cat', 'type': 'seq', 'minlen': 1, 'maxlen': 2}
        ], 'minlen':1, 'maxlen':1, 'type':'con'},
    scnd ={
       'attributes':[
            {'name': 'duration_s_cat', 'type': 'seq', 'minlen': 1, 'maxlen': 2}
        ], 'minlen':1, 'maxlen':1, 'type':'con'}
    )

res = hypo.result
current_dir = os.path.dirname(__file__)

all_hypotheses = []

for index in range(len(res["hypotheses"])):
    hypo = res["hypotheses"][index]
    all_hypotheses.append(HypothesisWraper("q7","sd4ft",hypo))

draw_double_fourfolds_greatest_deltapim(all_hypotheses, 10)