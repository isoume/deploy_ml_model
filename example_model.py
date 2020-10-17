#!/usr/bin/env python
# coding: utf-8

# # Example of machine learning model : Decision tree

# In[25]:


# For dataset example
from sklearn.datasets import load_iris
# For decision Tree
from sklearn import tree


# In[3]:


X, y = load_iris(return_X_y=True)


# In[4]:


clf = tree.DecisionTreeClassifier()


# In[26]:


# Training the model
clf = clf.fit(X, y)


# In[45]:


# Example of prediction 
clf.predict(X[1].reshape(1, -1))


# In[29]:


# For dumping the model like binary format
pickle.dump(clf, open('model.pkl', 'wb'))

