import pandas as pd

new_trials = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/trials_02.csv')
print(new_trials)

# new_trials = pd.melt(new_trials)
# print(new_trials)

new_trials = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/trials_02.csv')
new_trials = pd.melt(new_trials, id_vars=['treatment'])
print('id_vars', new_trials)


new_trials = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/trials_02.csv')
new_trials = pd.melt(new_trials, id_vars=['treatment'], value_vars=['F','M'])
print(new_trials)

new_trials = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/trials_02.csv')
new_trials = pd.melt(new_trials, id_vars=['treatment'], var_name='gender', value_name = 'response')
# NOTE: var_name and value_name is to give name to column
print(new_trials)
