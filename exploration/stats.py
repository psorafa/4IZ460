import os
import pandas as pd
import sys

print(sys.argv[1])

frame = pd.read_csv(sys.argv[1])

print(frame.describe())
