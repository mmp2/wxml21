import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.optimize import curve_fit
from sklearn import linear_model

# Define a linear regression function
def objective(x, a, b):
	return a * x + b

# Input all the csv files
data_df = pd.read_csv("Restaurants on the Ave.csv")
op_df = pd.read_csv("OP Ranking.csv")
fq_df = pd.read_csv("FQ Ranking.csv")
cs_df = pd.read_csv("CS Ranking.csv")
re_df = pd.read_csv("RE Ranking.csv")

# Set up several lists for us to revise in the future
op_total_ranking = [132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132]
fq_total_ranking = [132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132]
cs_total_ranking = [132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132]
re_total_ranking = [132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132, 132]

# Revise the lists we set up in the previous step
for i in range (0,11):
    for j in range (1,13):
        op_total_ranking[j-1] = op_total_ranking[j-1] - op_df.iloc[i,j]
        fq_total_ranking[j-1] = fq_total_ranking[j-1] - fq_df.iloc[i,j]
        cs_total_ranking[j-1] = cs_total_ranking[j-1] - cs_df.iloc[i,j]
        re_total_ranking[j-1] = re_total_ranking[j-1] - re_df.iloc[i,j]
        
# Prepare the information for plotting
fig, axs = plt.subplots(ncols=4, figsize=(80,20))
sns.pointplot(x=names, y=op_total_ranking, linestyles='-', hue=names, data=data_df, ax=axs[0])
sns.pointplot(x=names, y=fq_total_ranking, linestyles='-', hue=names, data=data_df, ax=axs[1])
sns.pointplot(x=names, y=cs_total_ranking, linestyles='-', hue=names, data=data_df, ax=axs[2])
sns.pointplot(x=names, y=re_total_ranking, linestyles='-', hue=names, data=data_df, ax=axs[3])
x1, y1 = fq_total_ranking, op_total_ranking
x2, y2 = cs_total_ranking, op_total_ranking
x3, y3 = re_total_ranking, op_total_ranking

# Plot the side-by-side dot plot
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

# Plot the linear regression plot
plt.figure(figsize =(15, 7))
plt.scatter(x1, y1)
plt.scatter(x2, y2)
plt.scatter(x3, y3)
plt.plot(x1_line, y1_line, color='purple')
plt.plot(x2_line, y2_line, color='orange')
plt.plot(x3_line, y3_line, color='green')
plt.xlabel("Borda Score for 3 criterias")
plt.ylabel("Overall Performance Borda Score")
plt.show()