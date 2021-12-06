from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.linear_model import LogisticRegressionCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import scale
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import sklearn.metrics as metrics
import pandas as pd
import matplotlib.pyplot as plt
import os

all_tracks = pd.read_csv("./output_data/dataset_categorised_2.csv")

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
cm_lr = metrics.confusion_matrix(y_test, y_pred_LR_cv)
print('Accuracy of Logistic Regression Model: ', accuracy_score(y_test, y_pred_LR_cv))

model_RF = RandomForestClassifier()
model_RF.fit(X_train, y_train)
y_pred_RF = model_RF.predict(X_test)
cm_rfc = metrics.confusion_matrix(y_test, y_pred_RF)
print('Accuracy of Random Forest Model: ', accuracy_score(y_test, y_pred_RF))

fig, (ax1, ax2) = plt.subplots(1,2, sharex=True, sharey=True, gridspec_kw={'width_ratios':[4,5]}) # při vynechání colorbaru se první graf zvětší, proto je potřeba přenastavit poměr
plot_confusion_matrix(model_LR_cv, X_test, y_test, cmap=plt.cm.Blues, ax = ax1, colorbar=False)
plot_confusion_matrix(model_RF, X_test, y_test, cmap=plt.cm.Blues, ax = ax2)
ax1.set(title='LinR')
ax2.set(title='RandF')
plt.show()
# plt.savefig("Confusion matrices RF and LR")
# plt.clf()

y_test_probs = model_LR_cv.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_test_probs)
roc_auc = roc_auc_score(y_test, y_test_probs)
plt.figure(0).clf()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='Linear Regression ROC (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC comparison LR x RFC')

y_test_probs = model_RF.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_test_probs)
roc_auc = roc_auc_score(y_test, y_test_probs)
plt.plot(fpr, tpr, color='lime',
         lw=lw, label='Random Forest ROC (area = %0.2f)' % roc_auc)
plt.legend(loc="lower right")
#plt.savefig("ROC curves for RF and LR")
plt.show()