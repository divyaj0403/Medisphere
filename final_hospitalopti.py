#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# In[59]:


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


# In[60]:


data=pd.read_csv("C:/Users/DIVYA/Desktop/Medisphere-2/dataset/hospitalopti.csv")


# In[61]:


data.head()


# In[62]:


data.info()


# In[65]:


categorical_columns = ['D.O.A','GENDER','RURAL','TYPE OF ADMISSION-EMERGENCY/OPD','DURATION OF STAY','OUTCOME']


# In[66]:


data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)


# In[67]:


data.to_csv("preprocessed_dataset2.csv", index=False)


# In[68]:


print(data.head())


# In[69]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# In[73]:


data = pd.read_csv("preprocessed_dataset2.csv")


# In[74]:


X = data.drop("OUTCOME_DISCHARGE", axis=1)  # Replace "TARGET_COLUMN" with the name of your target variable
y = data["OUTCOME_DISCHARGE"]


# In[75]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[76]:


model = LogisticRegression()


# In[77]:


model.fit(X_train, y_train)


# In[78]:


y_pred = model.predict(X_test)


# In[79]:


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))


# In[80]:


plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()


# In[81]:


from sklearn.metrics import roc_curve, roc_auc_score

y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.figure(figsize=(6,4))
plt.plot(fpr, tpr, color='darkorange', lw=2)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.show()


# In[ ]:




