import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

data_df = pd.read_csv("Restaurants on the Ave.csv")


vals_OP = []  # initializes a empty list to store overall performance scores for each resaurant 
vals_Conf = [] # initializes a empty list to store each participants' confidence scores

# store all the overall performance scores into vals_OP
for i in range(1, 13):
        vals_OP.append(data_df.iloc[:, i])

# store all the confidence score of overall performance scores into vals_Conf
for i in range(1, 13):
    vals_Conf.append(data_df.iloc[:, i+13])
    
# vals_weighted_score: store weighted score to vals_weighted_score

# the number to vals_weighted_score
vals_weighted_score = [] # initializes a empty list to store the weighted coefficient
                         # Rule for assigning weight coefficient:
                         # if Confidence score = 1, we give it the weighted coefficient of 1/6
                         # if Confidence score = 2, we give it the weighted coefficient of 1/3
                         # if Confidence score = 3, we give it the weighted coefficient of 1/2

vals_weighted_conf_score = []
for i in range(0, 12):
    vals_ind_score = []
    vals_ind_conf_score = []
    for j in range(0, 11):
        if vals_Conf[i].iloc[j] == 1:
            vals_ind_score.append(vals_OP[i].iloc[j]* 1/6)
            vals_ind_conf_score.append(1/6)
        elif vals_Conf[i].iloc[j] == 2:
            vals_ind_score.append(vals_OP[i].iloc[j]* 2/6)
            vals_ind_conf_score.append(2/6)
        else:
            vals_ind_score.append(vals_OP[i].iloc[j]* 3/6)
            vals_ind_conf_score.append(3/6)
    vals_weighted_score.append(vals_ind_score)
    vals_weighted_conf_score.append(vals_ind_conf_score)


vals_avg_score = [] # initializes a empty list to store each restaurants' average scores

# calculates and stores the average score invals_avg_score
for i in range(0, 12):
    vals_avg_score.append(sum(vals_weighted_score[i])/sum(vals_weighted_conf_score[i]))
    
    

names = [] # initializes a empty list to store the names of restaurants

for i in range(len(vals_OP)):
    names.append(vals_OP[i].name[133:-1]) 

import matplotlib.pyplot as plt

# plot bar graphs based on the overall performance scores
fig = plt.figure(figsize =(15, 7)) # set the figure size
plt.bar(names, vals_avg_score)  # plot a bar graph
plt.xticks(rotation=45, ha="right")  # rotate the x-axis tick value
plt.title("Average Scores for Restaurants on the Ave", fontsize = 30) # title
plt.xlabel("Restaurants") # x-axis label
plt.ylabel("Average Score") # y-axis label
plt.show() 



def objective(x, a, b):
	return a * x + b

op_df = pd.read_csv("OP Ranking.csv")
fq_df = pd.read_csv("FQ Ranking.csv")
cs_df = pd.read_csv("CS Ranking.csv")
re_df = pd.read_csv("RE Ranking.csv")

op_total_ranking = [132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132]
fq_total_ranking = [132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132]
cs_total_ranking = [132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132]
re_total_ranking = [132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132]

for i in range (0,11):
    for j in range (1,13):
        op_total_ranking[j-1] = op_total_ranking[j-1] - op_df.iloc[i,j]
        fq_total_ranking[j-1] = fq_total_ranking[j-1] - fq_df.iloc[i,j]
        cs_total_ranking[j-1] = cs_total_ranking[j-1] - cs_df.iloc[i,j]
        re_total_ranking[j-1] = re_total_ranking[j-1] - re_df.iloc[i,j]
        

fig, axs = plt.subplots(ncols=4, figsize=(80,20))
sns.pointplot(x=names, y=op_total_ranking, linestyles='-', hue=names, data=data_df, ax=axs[0])
sns.pointplot(x=names, y=fq_total_ranking, linestyles='-', hue=names, data=data_df, ax=axs[1])
sns.pointplot(x=names, y=cs_total_ranking, linestyles='-', hue=names, data=data_df, ax=axs[2])
sns.pointplot(x=names, y=re_total_ranking, linestyles='-', hue=names, data=data_df, ax=axs[3])

x1, y1 = op_total_ranking, fq_total_ranking
x2, y2 = op_total_ranking, cs_total_ranking
x3, y3 = op_total_ranking, re_total_ranking

popt1, _ = curve_fit(objective, x1, y1)
popt2, _ = curve_fit(objective, x2, y2)
popt3, _ = curve_fit(objective, x3, y3)
a1, b1 = popt1
a2, b2 = popt2
a3, b3 = popt3
x1_line = np.arange(min(x1), max(x1), 1)
x2_line = np.arange(min(x2), max(x2), 1)
x3_line = np.arange(min(x3), max(x3), 1)
y1_line = objective(x1_line, a1, b1)
y2_line = objective(x2_line, a2, b2)
y3_line = objective(x3_line, a3, b3)

plt.figure(figsize =(15, 7))
plt.scatter(x1, y1)
plt.scatter(x2, y2)
plt.scatter(x3, y3)
plt.plot(x1_line, y1_line, color='purple')
plt.plot(x2_line, y2_line, color='orange')
plt.plot(x3_line, y3_line, color='green')
plt.xlabel("Overall Performance")
plt.ylabel("Criteria Ranking Score")
plt.show() 