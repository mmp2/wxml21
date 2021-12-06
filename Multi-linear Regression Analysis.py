import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Load CSV files
op_df = pd.read_csv('OP Ranking.csv')
fq_df = pd.read_csv("FQ Ranking.csv")
cs_df = pd.read_csv("CS Ranking.csv")
re_df = pd.read_csv("RE Ranking.csv")

n_participant = 11  # number of participants
n_rest = 12       # number of restaurants

rank_cols_op = op_df.columns[1:]
rank_cols_fq = fq_df.columns[1:]
rank_cols_cs = cs_df.columns[1:]
rank_cols_re = re_df.columns[1:]
op_df = op_df[rank_cols_op]
fq_df = fq_df[rank_cols_fq]
cs_df = cs_df[rank_cols_cs]
re_df = re_df[rank_cols_re]

participant_list_op = {}
for i in range(1, n_participant + 1):
    participant_list_op[i] = op_df.iloc[i-1].to_numpy()

participant_list_fq = {}
for i in range(1, n_participant + 1):
    participant_list_fq[i] = fq_df.iloc[i-1].to_numpy()

participant_list_cs = {}
for i in range(1, n_participant + 1):
    participant_list_cs[i] = cs_df.iloc[i-1].to_numpy()

participant_list_re = {}
for i in range(1, n_participant + 1):
    participant_list_re[i] = re_df.iloc[i-1].to_numpy()


# Initialize Q_matrix
Q_matrix_op = dict()
for i in range(1, n_participant + 1):
    Q_matrix_op[i] = np.zeros((n_rest, n_rest))

Q_matrix_fq = dict()
for i in range(1, n_participant + 1):
    Q_matrix_fq[i] = np.zeros((n_rest, n_rest))

Q_matrix_cs = dict()
for i in range(1, n_participant + 1):
    Q_matrix_cs[i] = np.zeros((n_rest, n_rest))

Q_matrix_re = dict()
for i in range(1, n_participant + 1):
    Q_matrix_re[i] = np.zeros((n_rest, n_rest))


# Put appropriate values into Q_matrix
for i in range(1, n_participant + 1):
    for j in range(0, n_rest-1):
        pos = participant_list_op[i][j]
        for k in range(1, n_rest - j):
            temp = participant_list_op[i][n_rest - k]
            Q_matrix_op[i][pos-1, temp-1] = 1

for i in range(1, n_participant + 1):
    for j in range(0, n_rest-1):
        pos = participant_list_fq[i][j]
        for k in range(1, n_rest - j):
            temp = participant_list_fq[i][n_rest - k]
            Q_matrix_fq[i][pos-1, temp-1] = 1

for i in range(1, n_participant + 1):
    for j in range(0, n_rest-1):
        pos = participant_list_cs[i][j]
        for k in range(1, n_rest - j):
            temp = participant_list_cs[i][n_rest - k]
            Q_matrix_cs[i][pos-1, temp-1] = 1

for i in range(1, n_participant + 1):
    for j in range(0, n_rest-1):
        pos = participant_list_re[i][j]
        for k in range(1, n_rest - j):
            temp = participant_list_re[i][n_rest - k]
            Q_matrix_re[i][pos-1, temp-1] = 1


# Generate borda matrix
borda_matrix_op = np.zeros((n_rest, n_rest))
for i in range(1, n_participant + 1):
    borda_matrix_op += Q_matrix_op[i]

borda_matrix_fq = np.zeros((n_rest, n_rest))
for i in range(1, n_participant + 1):
    borda_matrix_fq += Q_matrix_fq[i]

borda_matrix_cs = np.zeros((n_rest, n_rest))
for i in range(1, n_participant + 1):
    borda_matrix_cs += Q_matrix_cs[i]

borda_matrix_re = np.zeros((n_rest, n_rest))
for i in range(1, n_participant + 1):
    borda_matrix_re += Q_matrix_re[i]


# Generate each restaurants' borda score in a list
final_borda_score_op = []
for i in range(0, n_rest):
    sum = 0
    for j in range(0, n_rest):
        sum += borda_matrix_op[j,i]
    final_borda_score_op.append(int(sum))
    sum = 0

final_borda_score_fq = []
for i in range(0, n_rest):
    sum = 0
    for j in range(0, n_rest):
        sum += borda_matrix_fq[j,i]
    final_borda_score_fq.append(int(sum))
    sum = 0

final_borda_score_cs = []
for i in range(0, n_rest):
    sum = 0
    for j in range(0, n_rest):
        sum += borda_matrix_cs[j,i]
    final_borda_score_cs.append(int(sum))
    sum = 0

final_borda_score_re = []
for i in range(0, n_rest):
    sum = 0
    for j in range(0, n_rest):
        sum += borda_matrix_re[j,i]
    final_borda_score_re.append(int(sum))
    sum = 0


# Prepare the list we need for linear regression analysis
num_val = n_rest * n_participant

op_total_ranking = [num_val] * n_rest
for i in range(0, n_rest):
    op_total_ranking[i] -= final_borda_score_op[i]

fq_total_ranking = [num_val] * n_rest
for i in range(0, n_rest):
    fq_total_ranking[i] -= final_borda_score_fq[i]

cs_total_ranking = [num_val] * n_rest
for i in range(0, n_rest):
    cs_total_ranking[i] -= final_borda_score_cs[i]

re_total_ranking = [num_val] * n_rest
for i in range(0, n_rest):
    re_total_ranking[i] -= final_borda_score_re[i]


# Multivariable Linear Regression Analysis
regr1 = linear_model.LinearRegression()


# Set up a dataframe
data = {'fq_total_ranking': fq_total_ranking, 'cs_total_ranking': cs_total_ranking, 're_total_ranking': re_total_ranking,  'op_total_ranking': op_total_ranking}
df = pd.DataFrame(data=data)


# Build a model by using borda's rule
X = df[['fq_total_ranking', 'cs_total_ranking', 're_total_ranking']]
y = df['op_total_ranking']
model = regr1.fit(X, y)


# Print coefficient values
print('In this multiple regression analysis, we apply borda scores of each critierias. \nThe coefficient between overall performance and food quality is',
 regr1.coef_[0],'\nThe coefficient between overall performance and customer service is', regr1.coef_[1],
 '\nThe coefficient between overall performance and restaurant environment is', regr1.coef_[2])

# Visualize the data simply by using side-by-side plots
sns.set_palette('colorblind')
sns.pairplot(data=df, height=3)

# Prepare data for 3D plots
X = df[['cs_total_ranking', 're_total_ranking']].values.reshape(-1,2)
Y = df['fq_total_ranking']


# Create range for each dimension
x = X[:, 0]
y = X[:, 1]
z = Y

xx_pred = np.linspace(30, 120, 30)
yy_pred = np.linspace(30, 120, 30)
xx_pred, yy_pred = np.meshgrid(xx_pred, yy_pred)
model_viz = np.array([xx_pred.flatten(), yy_pred.flatten()]).T


# Predict using model
ols = linear_model.LinearRegression()
model = ols.fit(X, Y)
predicted = model.predict(model_viz)


# Evaluate model by using it's R^2 score 
r2 = model.score(X, Y)


# Plot model visualization
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')
axes = [ax1, ax2, ax3]


# Build the 3D plot
for ax in axes:
    ax.plot(x, y, z, color='k', zorder=15, linestyle='none', marker='o', alpha=0.5)
    ax.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, facecolor=(0,0,0,0), s=20, edgecolor='#70b3f0')
    ax.set_xlabel('Customer Service', fontsize=12)
    ax.set_ylabel('Restaurant Environment', fontsize=12)
    ax.set_zlabel('Food Quality', fontsize=12)
    ax.locator_params(nbins=4, axis='x')
    ax.locator_params(nbins=5, axis='x')

ax1.view_init(elev=25, azim=-60)
ax2.view_init(elev=15, azim=15)
ax3.view_init(elev=25, azim=60)


# Show the 3D plot, which indicates the relationship between food quality, customer service, and restaurant environment
fig.suptitle('Multi-Linear Regression Model Visualization ($R^2 = %.2f$)' % r2, fontsize=15, color='k')
fig.tight_layout()


# Show the 3D plot, which indicates the relationship between food quality, customer service, and restaurant environment
fig.suptitle('Multi-Linear Regression Model Visualization ($R^2 = %.2f$)' % r2, fontsize=15, color='k')
fig.tight_layout()
