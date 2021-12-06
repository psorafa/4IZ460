from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.linear_model import LogisticRegressionCV
from sklearn.preprocessing import scale
from sklearn.metrics import accuracy_score
import sklearn.metrics as metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


# all_tracks = pd.read_csv("./output_data/dataset_merged_with_eras_pt1.csv")
all_tracks = pd.read_csv("./output_data/dataset_categorised_pt1.csv")

features = ['danceability', 'energy', 'key', 'loudness',
       'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'time_signature', 'chorus_hit', 'duration_s',
       'sections']

X = all_tracks[features]
y = all_tracks['hit']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42) 

model_LR_cv = LogisticRegressionCV(cv=3,Cs=5,scoring = "accuracy")
model_LR_cv.fit(X_train, y_train)
y_pred_LR_cv = model_LR_cv.predict(X_test)

# fig, ax = plt.subplots(figsize=(15,5))
# plot_confusion_matrix(model_LR_cv, X_test, y_test, cmap=plt.cm.Blues, ax = ax)
# ax.set(title='Confusion matrix for Logistic Regression')
# plt.show()

cm_rfc = metrics.confusion_matrix(y_test, y_pred_LR_cv)

print(accuracy_score(y_test, y_pred_LR_cv))

mpl.rcParams['figure.figsize']=(6,5)
fig, ax = plt.subplots()

sns.heatmap(pd.DataFrame(cm_rfc), annot=True, cmap="PuBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix for Logistic Regression', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label', labelpad=15)
plt.show()

# all_songs_coef = model_LR_cv.coef_
# df_all_songs_coefs = pd.DataFrame(all_songs_coef)
# print(df_all_songs_coefs)
# analyzovat koeficienty LR dava smysl jen pokud by cely model byl slozen z normalizovanych hodnot, coz nemame

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

y_test_probs = model_LR_cv.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_test_probs)
roc_auc = roc_auc_score(y_test, y_test_probs)
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Logistic Regression ROC curve')
plt.legend(loc="lower right")
plt.show()