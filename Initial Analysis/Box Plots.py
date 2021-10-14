
# coding: utf-8

# In[87]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[88]:


data_df = pd.read_csv("Dataset.csv")


# In[89]:


vals =[]
names = []
for i in range(1, 13):
    vals.append(data_df.iloc[:,i])


# In[90]:


for i in range(len(vals)):
    names.append(vals[i].name[133:-1])


# In[93]:


fig = plt.figure(figsize =(20, 7))
ax = fig.add_subplot(111)
plt.boxplot(vals)
plt.setp(ax, xticklabels=names)
plt.title("Box Plots of Overall Restaurant Ratings")
plt.ylabel("Score")
plt.show()

