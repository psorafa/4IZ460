import os
import pandas as pd
import sys

print(sys.argv[1])

frame = pd.read_csv(sys.argv[1])

print(frame.describe())

#explore_types = ["int64", "float64"]
#
#for (column, type) in frame.dtypes.iteritems():
#
#    if type in explore_types:
#        