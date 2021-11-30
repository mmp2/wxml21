"""
This is the code for Borda's Rule

Q_matrix displays the consensus ranking of restaurants into matrix. 
Borda Score and inversion distance can also be shown in Q_matrix.

In this code, we will show 
(1) the Q_matrix, borda score, inversion distance, inversion sum of each participants 
(2) final borda matrix and borda score
(3) the final ranking of restaurants 


We use number to indicate different restaurants
1, 'Chipotle',
2, 'Memos Mexican Food Restaurant',
3, 'U:Don Fresh Japanese Noodle Station',
4, "Costa's Restaurant",
5, 'Thai Tom',
6, 'Palmi Korean BBQ',
7, 'Chi Mac',
8, "Taste of Xi'an",
9, 'Just Burgers',
10, 'Korean Tofu House',
11, 'Shawarma King',
12, 'Pho Shizzle'



Final Ranking: 
    
1. Palmi Korean BBQ
2. Shawarma King
3. Chipotle
4. Korean Tofu House
5. Costa's Restaurant
6. Thai Tom
7. Taste of Xi'an
8. Pho Shizzle
9. Chi Mac
10. U:Don Fresh Japanese Noodle Station
11. Just Burgers
12. Memos Mexican Food Restaurant


"""

# Import packges
import pandas as pd
import numpy as np
from collections import defaultdict

# Load Overall-Performance CSV file
df = pd.read_csv('WXML dataset - OP Ranking.csv')

rank_cols = df.columns[1:]
df = df[rank_cols]

n_participant = len(df.index)  # number of participants
n_rest = len(df.columns)       # number of restaurants

## Q_matrix

# store each row, which is the ranking by each participant, 
# in the dataframe into dictionary
participant_list = {}
for i in range(1, n_participant + 1):
    participant_list[i] = df.iloc[i-1].to_numpy()

# initialize Q_matrix for each participant
Q_matrix = dict()
for i in range(1, n_participant + 1):
    Q_matrix[i] = np.zeros((n_rest, n_rest))

# structure Q_matrix
for i in range(1, n_participant + 1):
    for j in range(0, n_rest-1):
        pos = participant_list[i][j]
        for k in range(1, n_rest - j):
            temp = participant_list[i][n_rest - k]
            Q_matrix[i][pos-1, temp-1] = 1
            

## Inversion Distance

# initialize a dictionary to store the inversion distance
inversion_list = {}
for i in range(1, n_participant + 1):
    inversion_list[i] = []

# generate inversion distance of each participant
for i in range(1, n_participant + 1):
    matrix = Q_matrix[i]
    for j in range(0, n_rest - 1):
        value = 0
        for k in range(j + 1, n_rest):
            if matrix[k,j] == 1:
                value += 1;
        inversion_list[i].append(value)
        value = 0


## Inversion Sum

# initialize a dictionary to store the inversion sum
inversion_sum = {}
for i in range(1, n_participant + 1):
    inversion_sum[i] = 0

# generate inversion sum of each participant
for i in range(1, n_participant + 1):
    sum = 0
    for j in range(0, len(inversion_list[1])):
        element = inversion_list[i][j]
        sum += element
    inversion_sum[i] = sum


## Borda Score

# initialize a dictionary to store the borda score
borda_score = {}
for i in range(1, n_participant + 1):
    borda_score[i] = []

# generate borda score of each participant
for i in range(1, n_participant + 1):
    matrix = Q_matrix[i]
    for j in range(0, n_rest):
        sum = 0
        for k in range(0, n_rest):
            sum += matrix[k, j]
        borda_score[i].append(int(sum))
        sum = 0


## Final Borda Matrix

# generate the final borda matrix
borda_matrix = np.zeros((n_rest, n_rest))
for i in range(1, n_participant + 1):
    borda_matrix += Q_matrix[i]

## Final Borda Score

# generate the final borda score
final_borda_score = []
for i in range(0, n_rest):
    sum = 0
    for j in range(0, n_rest):
        sum += borda_matrix[j,i]
    final_borda_score.append(int(sum))
    sum = 0
    

## put the restaurants and borda score together

scores = defaultdict(int)      # initialize a dictionary for storing scores

# Store scores to dictionary
#
# dictionary.key: index that indicates restaurants
# dictionary.value: scores

for i in range(0, n_participant):
    for j in range(0, n_rest):
        key = df.iat[i,j]
        if key in scores:
            scores[key] += j
        else: 
            scores[key] = j
            
            
names = list(df)    # list of restaurants
scores_table = defaultdict(int)   # Initialize a dictionary that stores restaurant name and scores

# Store restaurant names as key and also save the corresponding score
for j in range(0, n_rest):
        if (j+1) in scores:
            scores_table[names[j]] = scores[j+1]
        
# Sort the score_table by value
sorted_scores = sorted(scores_table.items(), key=lambda kv: kv[1])
# Print sorted_scores dictionary

# initialize a dictionary to store the final ranking
final_ranking = {}
for i in range(0, n_rest):
    final_ranking[i] = ""
    
# store the ranked restuarant names into the dictionary
for i in range(0, n_rest):
    rest_name = sorted_scores[i][0]
    final_ranking[i+1] = "{0}. ".format(i+1) + rest_name
    
        

## Print out all the results

# Q_matrix, borda score, inversion distance, inversion sum for each participant
for i in range(1, n_participant + 1):
    print("Q_matrix_{0}".format(i) + ": ")
    print(Q_matrix[i])
    print("Borda Score: ")
    print(borda_score[i])
    print("Inversion Distance: ")
    print(inversion_list[i])
    print("Inversion Sum: ")
    print(inversion_sum[i])
    print("-------")

# final borda matrix
print("Borda Matrix: ")
print(borda_matrix)
# final borda score
print("Borda Score: ")
print(final_borda_score)
print("-------")

# print out the final ranking of restaurants with borda score
print("Final Ranking with Borda Scores: ")
for i in range(0, n_rest):
    print(sorted_scores[i])
print("-------")

# print out the final ranking of restaurants without borda score
print("Final Ranking: ")
for i in range(1, n_rest + 1):
    print(final_ranking[i])
    



            
