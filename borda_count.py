
"""
This is the code for Borda's Rules

Results:
    
('Palmi Korean BBQ', 37),
('Shawarma King', 49),
('Chipotle', 51), 
'Korean Tofu House', 58), 
("Costa's Restaurant", 59),
('Thai Tom', 59),
("Taste of Xi'an", 61), 
('Pho Shizzle', 62),
('Chi Mac', 65),
('U:Don Fresh Japanese Noodle Station', 70), 
('Just Burgers', 76), 
('Memos Mexican Food Restaurant', 79)

Restaurants with lower scores have higher ranking.


In order to demonstrate the code and how it's being implemented,
here's an example:

#1:    [a b c d]
score: [0 1 2 3]

#2:    [d a c b]
score: [1 3 2 0]

# 3:   [c b a d]
score: [2 1 0 3]

Total score: [a b c d] = [3 5 4 6]

Final Borda Rank: [a c b d] = [3 4 5 6]


"""

# Import packges
import pandas as pd
from collections import defaultdict

# Load Overall-Performance CSV file
df = pd.read_csv('WXML dataset - OP Ranking.csv')

rank_cols = df.columns[1:]
df = df[rank_cols]

n_participant = len(df.index)  # number of participants
n_rest = len(df.columns)       # number of restaurants
scores = defaultdict(int)      # initialize a dictionary for storing scores

# Store scores to dictionary
#
# We use number to indicate different restaurants
# 1, 'Chipotle',
# 2, 'Memos Mexican Food Restaurant',
# 3, 'U:Don Fresh Japanese Noodle Station',
# 4, "Costa's Restaurant",
# 5, 'Thai Tom',
# 6, 'Palmi Korean BBQ',
# 7, 'Chi Mac',
# 8, "Taste of Xi'an",
# 9, 'Just Burgers',
# 10, 'Korean Tofu House',
# 11, 'Shawarma King',
# 12, 'Pho Shizzle'
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
scores_table = defaultdict(int)   # Initialize a dictionary that stores
                                  # restaurant name and scores

# Store restaurant names as key and also save the corresponding score
for j in range(0, n_rest):
        if (j+1) in scores:
            scores_table[names[j]] = scores[j+1]
        
# Sort the score_table by value
sorted_scores = sorted(scores_table.items(), key=lambda kv: kv[1])
# Print sorted_scores dictionary
print(sorted_scores)




