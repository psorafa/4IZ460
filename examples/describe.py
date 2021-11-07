import sys
import pandas as pd
import matplotlib.pyplot as plt

print(sys.argv[1])

df = pd.read_csv(sys.argv[1])

print(len(list(df.columns)))

print(df['hit'].value_counts())