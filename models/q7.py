import pandas as pd
import sys
from cleverminer.cleverminer import cleverminer
import matplotlib.pyplot as plt
import os
import numpy as np
from hypothesis import HypothesisWraper
from hypothesis import draw_double_fourfolds_greatest_deltapim

# takto položená otázka bude dávat lepší sm

df = pd.read_csv(
    "./output_data/dataset_categorised_2.csv",
    usecols=["danceability_cat", "instrumentalness_cat", "acousticness_cat", "era", "hit"],
    dtype={
        "danceability_cat": "category",
        "instrumentalness_cat": "category",
        "acousticness_cat": "category",
        "era": "category",
        "hit": "int64"
    }
)

hypo = cleverminer(df=df,proc='SD4ftMiner',
    quantifiers= {'Base1':200, 'Base2':200, 'Deltapim' : 0.4},
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
            {'name': 'era', 'type': 'subset', 'minlen': 1, 'maxlen': 3}
        ], 'minlen':1, 'maxlen':1, 'type':'con'},
    scnd ={
       'attributes':[
            {'name': 'era', 'type': 'subset', 'minlen': 1, 'maxlen': 3}
        ], 'minlen':1, 'maxlen':1, 'type':'con'}
    )

res = hypo.result
current_dir = os.path.dirname(__file__)

all_hypotheses = []

for index in range(len(res["hypotheses"])):
    hypo = res["hypotheses"][index]
    all_hypotheses.append(HypothesisWraper("q7","sd4ft",hypo))

draw_double_fourfolds_greatest_deltapim(all_hypotheses, 10)