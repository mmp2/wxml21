"""
This code calculates the average score of restaurants on the Ave
and plot a bar plot.

"""

# import packages
import matplotlib.pyplot as plt
import pandas as pd

# import file
data_df = pd.read_csv("Restaurants on the Ave.csv")


vals_OP = []  # stores overall performance score
vals_Conf = [] # stores confidence scores of the oeveral performance score

# store all the overall performance scores into vals_OP
for i in range(1, 13):
        vals_OP.append(data_df.iloc[:, i])

# store all the confidence score of overall performance scores into vals_Conf
for i in range(1, 13):
    vals_Conf.append(data_df.iloc[:, i+13])
    
# vals_weighted_score: store weighted score to vals_weighted_score
# if Confidence score = 1, we give it the weight of 1/6
# if Confidence score = 2, we give it the weight of 2/6
# if Confidence score = 2, we give it the weight of 3/6
# We multiplied each overal performance score by its weights and then store
# the number to vals_weighted_score
vals_weighted_score = []
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


vals_avg_score = []   # stores the average scores

# calculate and store the average score
for i in range(0, 12):
    vals_avg_score.append(sum(vals_weighted_score[i])/sum(vals_weighted_conf_score[i]))
    
    
# store the names of restaurants
names = []
for i in range(len(vals_OP)):
    names.append(vals_OP[i].name[133:-1]) 


# plot the graph
fig = plt.figure(figsize =(15, 7)) # set the figure size
plt.bar(names, vals_avg_score)  # plot a bar graph
plt.xticks(rotation=45, ha="right")  # rotate the x-axis tick value
plt.title("Average Scores for Restaurants on the Ave", fontsize = 30) # title
plt.xlabel("Restaurants") # x-axis label
plt.ylabel("Average Score") # y-axis label
plt.show() 
