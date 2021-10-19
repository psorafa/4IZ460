import pandas as pd
import sys

from cleverminer.cleverminer import cleverminer

df = pd.read_csv ('HotelPlusExternal.Export.txt', encoding='cp1250', sep='\t')
df=df[['VTypeOfVisit','GState','GCity','WSky','GSex']]

hypo = cleverminer(
    df=df,
    proc='4ftMiner',
    quantifiers= {'pim':0.6, 'Base':50},
    ante ={
        'attributes':[
            {'name': 'GState', 'type': 'subset', 'minlen': 1, 'maxlen': 1}
        ], 'minlen':1, 'maxlen':2, 'type':'con'},
    succ ={
        'attributes':[
            {'name': 'VTypeOfVisit', 'type': 'subset', 'minlen': 1, 'maxlen': 1}
        ], 'minlen':1, 'maxlen':2, 'type':'con'},
    cond ={
        'attributes':[
            {'name': 'GCity', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
            {'name': 'GSex', 'type': 'subset', 'minlen': 1, 'maxlen': 2}
        ], 'minlen':1, 'maxlen':2, 'type':'con'}
    ).result
    
print(hypo)