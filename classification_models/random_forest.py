from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import scale
from sklearn.metrics import accuracy_score
from sklearn import metrics
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


all_tracks = pd.read_csv("./output_data/dataset_categorised.csv")

features = ['danceability', 'energy', 'key', 'loudness',
       'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'duration_s', 'time_signature', 'chorus_hit',
       'sections']

X = all_tracks[features]
y = all_tracks['hit']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42) 

model_RF = RandomForestClassifier()
model_RF.fit(X_train, y_train)
y_pred_RF = model_RF.predict(X_test)
cm_rfc = metrics.confusion_matrix(y_test, y_pred_RF)

print(accuracy_score(y_test, y_pred_RF))

mpl.rcParams['figure.figsize']=(6,5)
fig, ax = plt.subplots()

# seaborn heatmap
sns.heatmap(pd.DataFrame(cm_rfc), annot=True, cmap="PuBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix for Random Forrest Classifier', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label', labelpad=15)
plt.show()

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

#ROC curve - Random forest
y_test_probs = model_RF.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_test_probs)
roc_auc = roc_auc_score(y_test, y_test_probs)
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='lime',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='teal', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Random forest ROC curve')
plt.legend(loc="lower right")
plt.show()