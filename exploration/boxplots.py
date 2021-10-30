import pandas as pd
import sys
import matplotlib.pyplot as plt
import os

dirname = os.path.dirname(__file__)

print(sys.argv[1])

frame = pd.read_csv(sys.argv[1])

explore_types = ["int64", "float64"]

for (column, type) in frame.dtypes.iteritems():

    if column == "Unnamed: 0":
        continue

    if type in explore_types:
        boxplot = frame[column].plot(
             kind='box',
             color=dict(boxes='r', whiskers='r', medians='g', caps='r'),
             boxprops=dict(linestyle='-', linewidth=1.5),
             flierprops=dict(linestyle='-', linewidth=1.5),
             medianprops=dict(linestyle='-', linewidth=1.5),
             whiskerprops=dict(linestyle='-', linewidth=1.5),
             capprops=dict(linestyle='-', linewidth=1.5),
             showfliers=False,
             showmeans=True,
             grid=True,
             rot=0
        )

        fig = boxplot.get_figure()

        plt.savefig(os.path.join(dirname, "out", "boxplots", column + ".png"))
        plt.close(fig)