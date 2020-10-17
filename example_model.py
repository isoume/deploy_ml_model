#!/usr/bin/env python
# coding: utf-8

# Example of machine learning model : Decision tree

# For dataset example
from sklearn.datasets import load_iris
# For decision Tree
from sklearn import tree


X, y = load_iris(return_X_y=True)
clf = tree.DecisionTreeClassifier()

# Training the model
clf = clf.fit(X, y)

# Example of prediction 
clf.predict(X[1].reshape(1, -1))

# For dumping the model like binary format
pickle.dump(clf, open('model.pkl', 'wb'))

