import pandas as pd

election = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/pennsylvania2012_turnout.csv', index_col='county')

# slicing rows
p_counties = election['Perry':'Potter']
# print(p_counties)
# p_counties_rev = election['Potter':'Perry':-1] # NOTE: -1 the step tp reverse
# print(p_counties_rev)

# slicing columns
left_columns = election.loc[:,'Obama']
# print(left_columns)
# middle_column = election.loc[:,'Obama':'winner']
# print(middle_column.head())
# right_column = election.loc[:,'Romney':]
# print(right_column.head())

# subselecting with list
rows = ['Philadelphia', 'Centre', 'Fulton']
cols = ['winner', 'Obama', 'Romney']
there_counties = election.loc[rows,cols]
print(there_counties.head())
