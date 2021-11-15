import os
import pandas as pd
import pprint as pprint
import re

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, '..' + os.sep + 'data' + os.sep)
outpath1 = os.path.join(dirname, '..' + os.sep + 'output_data' + os.sep, "dataset_merged_with_eras_pt1.csv")
outpath2 = os.path.join(dirname, '..' + os.sep + 'output_data' + os.sep, "dataset_merged_with_eras_pt2.csv")

frames1 = []
frames2 = []

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

            if era[0] == '80' or era[0] == '90':
                frames1.append(frame)
            if era[0] == '00' or era[0] == '10':
                frames2.append(frame)

    break

result1 = pd.concat(frames1,ignore_index=True)
result2 = pd.concat(frames2,ignore_index=True)
print(result1)
print(result2)
result1.to_csv(outpath1, index=False)
result2.to_csv(outpath2, index=False)