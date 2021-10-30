import os
import pandas as pd
import pprint as pprint
import re

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, '..' + os.sep + 'data' + os.sep)
outpath = os.path.join(dirname, '..' + os.sep + 'output_data' + os.sep, "dataset_merged_with_eras.csv")

frames = []

for (dirpath, dirnames, filenames) in os.walk(path):

    for filename in filenames:
        path = os.path.join(dirname, '..' + os.sep + 'data', filename)
        filename, file_extension = os.path.splitext(path)

        era = re.findall('dataset-of-(\d\d)s', filename)
        
        if file_extension == ".csv":
            frame = pd.read_csv(path)

            frame.rename(
                columns={"target": "hit"},
                inplace=True
            )

            frame["era"] = era[0]

            frames.append(frame)

    break

result = pd.concat(frames,ignore_index=True)
print(result)
result.to_csv(outpath, index=False)