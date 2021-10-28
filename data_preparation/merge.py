import os
import pandas as pd
import pprint as pprint

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, '../data/')

frames = []

for (dirpath, dirnames, filenames) in os.walk(path):
    print(filenames)
    frames.extend(pd.read_csv(filenames))
    break

result = pd.concat(frames,ignore_index=True)
pprint(result)