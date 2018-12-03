import numpy as np
from sklearn import model_selection, svm
import pandas as pd

df = pd.read_csv('../spambase.data.txt')

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.30)

clf = svm.SVC(kernel='linear', C=1, gamma=1) 

clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)                                   