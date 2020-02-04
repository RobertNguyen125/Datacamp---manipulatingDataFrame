import pandas as pd

election = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/pennsylvania2012_turnout.csv', index_col='county')
print(election.columns)

x = 4
y = 4

print(election.iloc[x,y]==election.loc['Bedford', 'winner'])

# indexing and column rearrangement
results = election[['winner', 'total', 'voters']]
print(results.head())

# select a column (Series)
