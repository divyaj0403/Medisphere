#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd


# In[23]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# In[24]:


data=pd.read_csv("C:/Users/DIVYA/Desktop/Medisphere-2/dataset/ProjectData - PATIENT OUTCOME.csv")


# In[25]:


data.head()


# In[26]:


data.info()


# In[27]:


categorical_columns = ['NOP(DEPT)']


# In[28]:


data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)


# In[29]:


print(data.head())


# In[30]:


data.to_csv("preprocessed_dataset.csv", index=False)


# In[31]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# In[32]:


data = pd.read_csv("preprocessed_dataset.csv")


# In[33]:


X = data.drop("READMITTED (yes=1/no=0)", axis=1)  # Replace "TARGET_COLUMN" with the name of your target variable
y = data["READMITTED (yes=1/no=0)"]


# In[34]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[35]:


model = LogisticRegression()


# In[36]:


model.fit(X_train, y_train)


# In[37]:


y_pred = model.predict(X_test)


# In[38]:


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))


# In[40]:


plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()


# In[42]:


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




