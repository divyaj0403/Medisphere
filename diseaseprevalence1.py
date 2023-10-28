#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
import pickle
warnings.filterwarnings("ignore")
import math


# In[18]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


data=pd.read_csv("C:/Users/DIVYA/Desktop/Medisphere-2/dataset/ProjectData - DISEASE PREVELANCE.csv")


# In[7]:


data.head()


# In[8]:


data.info()


# In[21]:


categorical_columns = ['DISEASE','AREA(D=DOMBIVLI/V=VASAI)']


# In[22]:


data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)


# In[ ]:


data.to_csv("preprocessed_dataset1.csv", index=False)


# In[12]:


print(data.head())


# In[13]:


X = data.drop("AREA(D=DOMBIVLI/V=VASAI)_VASAI", axis=1)  # Replace "TARGET_COLUMN" with the name of your target variable
y = data["AREA(D=DOMBIVLI/V=VASAI)_VASAI"]


# In[14]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[15]:


model = LogisticRegression()


# In[16]:


model.fit(X_train, y_train)
pickle.dump(model,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


# In[17]:


#y_pred = model.predict(X_test)


# In[11]:


#accuracy = accuracy_score(y_test, y_pred)
#print("Accuracy:", accuracy)
#print("\nClassification Report:\n", classification_report(y_test, y_pred))
#print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))


# In[19]:


"""plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()"""


# In[20]:


"""from sklearn.metrics import roc_curve, roc_auc_score

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
plt.show()"""


# In[ ]:




