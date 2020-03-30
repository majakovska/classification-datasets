from sklearn.model_selection import train_test_split, GridSearchCV
import pandas as pd
import sklearn.metrics as met
import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import sklearn.preprocessing as prep

from sklearn.decomposition import PCA


df = pd.read_csv('substracted.csv')
df = df.drop(columns='SvGms_diff', axis=1)

df = df.dropna()


y = df['outcome']
x = df.drop(columns = 'outcome', axis = 1)
# x = x.dropna()
# x = x.drop(columns = 'SvGms_diff', axis = 1)

# for col in x.columns :

# 	print(x[col].unique())

# print(y.head())
# print("lalala")
# print(x.columns)


# pca = PCA()
# pca.fit(x)

# x = pd.DataFrame(pca.transform(x))

# sums = np.cumsum(pca.explained_variance_ratio_)

# print(pca.explained_variance_ratio_)

x_train, x_test, y_train, y_test = train_test_split(x, y, stratify = y, test_size = 0.3)

# print(x_train.head())


parameters_for_KNN = [
                {'n_neighbors': [3, 4, 5],
               'weights' : ['distance', 'uniform'], 
                'p' : [1, 2]
               }]

parameters_for_SVC = [{'C': [pow(2,x) for x in range(-6,10,2)],
               'kernel' : ['linear']
               },

              {'C': [pow(2,x) for x in range(-6,10,2)],
               'kernel': ['poly'],
               'degree': [2, 3, 4, 5],
               'gamma': np.arange(0.1, 1.1, 0.1),
               'coef0': np.arange(0, 2, 0.5)
               },

                {'C': [pow(2,x) for x in range(-6,10,2)],
               'kernel' : ['rbf'],
               'gamma': np.arange(0.1, 1.1, 0.1),
               },

               {'C': [pow(2,x) for x in range(-6,10,2)],
               'kernel' : ['sigmoid'],
               'gamma': np.arange(0.1, 1.1, 0.1),
               'coef0': np.arange(0, 2, 0.5)
               }]

clf = GridSearchCV(KNeighborsClassifier(), parameters_for_KNN, cv=5, scoring='precision_macro')
clf.fit(x_train, y_train)

y_predicted = clf.predict(x_test)

print(clf.best_score_)
print(clf.best_params_)

y_predicted = clf.predict(x_test)

print(met.confusion_matrix(y_test, y_predicted))
print(len(y_train))

df_players = pd.read_csv('grouped_players.csv')

df_players = df_players.drop(columns = 'w_SvGms', axis = 1)
# print(df_players.columns)
# df = df.drop(columns='w_SvGms', axis=1)

df_players.set_index('winner_id', inplace=True, drop=True)

player1 = df_players.ix[201311]
player2 = df_players.ix[201320]

real = player1 - player2
# print(real)

print(np.array(x_test).shape)

reshaped = np.array(real).reshape(1, 10)
print(reshaped.shape)


y_predicted = clf.predict(reshaped)

print(y_predicted)

