import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import os

# 2.	Jaké faktory nejvíce korelují s faktem, že se skladba stala hitem?

# Pro zodpovězení těto otázky použijeme vlasností nejlepšího modelu klasifikátoru Random Forest.

all_tracks = pd.read_csv("./output_data/dataset_categorised_2.csv")

features = ['danceability', 'energy', 'key', 'loudness',
       'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'duration_s', 'time_signature', 'chorus_hit',
       'sections']

X = all_tracks[features]
y = all_tracks['hit']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42) 

model_RF = RandomForestClassifier()
model_RF.fit(X_train, y_train)

all_songs_feat = model_RF.feature_importances_
df_indep_columns = pd.DataFrame(features)
df_all_songs_feat = pd.DataFrame(all_songs_feat)
all_songs_feat_vars = pd.concat([df_indep_columns, df_all_songs_feat], axis = 1)
all_songs_feat_vars.columns = ['Variable', 'Feature importance']
all_songs_feat_vars = all_songs_feat_vars.set_index('Variable')
all_songs_feat_vars = all_songs_feat_vars.sort_values(by=['Feature importance'], ascending = False)

# print(all_songs_feat_vars)
outpath = os.path.join(os.path.dirname(__file__) + os.sep + 'q2', "q2_features.txt")
outfile = open(outpath, "w")
outfile.writelines(all_songs_feat_vars.to_string(header=True, index=True))
outfile.close()