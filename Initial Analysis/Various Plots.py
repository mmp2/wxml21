
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import itertools

# Accepts 'rankings.txt' which is generated from the Mallows Model Code
# Must have no header and be whitespace separated
data_df = pd.read_csv("rankings.txt", header=None, delim_whitespace=True)


# In[2]:


# Encode modal ranking found from Mallows Model and calculate ranking frequencies
modal = [6,11,1,4,10,12,5,8,3,7,9,2]
ranking_freq = [[0 for i in range(12)] for j in range(12)]
for i in range(len(modal)):
    restaurant = modal[i]
    ranks = data_df.iloc[:][i]
    for j in range(len(ranks)):
        rank = ranks[j]
        ranking_freq[restaurant-1][rank-1]+=1
    


# In[4]:


# Generate stacked barplot showcasing relative ranking frequencies
# restaurants are on the x axis, rankings are shown in colors
labels = ['U:Don', 'Pho Shizzle', 'Just Burgers', 'Costas', 'Chi Mac', 'Chipotle', 'Korean Tofu House', 'Taste of Xian', 'Shawarma King', 'Thai Tom', 'Memos','Palmi']
ranking_df = pd.DataFrame(ranking_freq, columns = range(1,13))
ranking_df.index=labels
ranking_df.plot(kind='bar', stacked=True, figsize=(20, 10), colormap="GnBu")
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", fontsize=16)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 16)
plt.ylabel('Frequency of Rank', fontsize=16)
plt.title('Frequency of Ranks for Each Restaurant', fontsize=16)
plt.savefig('RankFreq_V1.png', bbox_inches='tight')


# In[23]:


# Inverted stacked barplot as above. Rank is on the x axis and restaurants
# are colors. Might not be as useful.
ranking_df_T = ranking_df.T
ranking_df_T.plot(kind='bar', stacked=True, figsize=(20, 10), colormap="GnBu")
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", fontsize = 14)
plt.xticks(rotation=0, fontsize = 16)
plt.yticks(fontsize=16)
plt.savefig('RankFreq_V2.png', bbox_inches='tight')


# In[15]:


# Generate Bump Plot with Participant on x axis and restaurant as color
# Might not be as useful as bump plot below
fig, ax = plt.subplots()
cmap = plt.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 1, len(labels))]

for i, color in enumerate(colors):
    pos = modal[i]
    curr_label = labels[pos-1]
    plt.plot(data_df.iloc[:][i], "o-", label=curr_label, color = color)

ax.set(xlabel='Participant',ylabel='Restaurant Rank',
       title='Rank Bump Plot')
ax.set_xticks(range(12))
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
plt.savefig("BumpPlot.png",  bbox_inches='tight')


# In[39]:


# Cleaner Bump Plot with Participants as colors and restuarants
# on the axis
plt.figure(figsize=(20,10)) 
cmap = plt.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 1, 11)]

for i, color in enumerate(colors):
    participant_ranks = []
    for j in modal:
        participant_ranks.append(data_df.iloc[i][j-1])
    label = 'Participant '+ str(i+1)
    plt.plot(participant_ranks, "o-", label=label, color = color)

plt.title('Rank Bump Plot', fontsize=16)
plt.ylabel('Ranking', fontsize=16)
plt.xticks(range(12), labels, rotation=90, fontsize=14)
plt.yticks(fontsize=14)
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
plt.savefig("BumpPlot.png",  bbox_inches='tight')

