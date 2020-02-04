import pandas as pd
import numpy as np
election = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/pennsylvania2012_turnout.csv', index_col='county')

# create boolean array: high_turnout where the turnout rate is > 70
high_turnout = election['turnout'] > 70

# filter the df
high_turnout_df = election[high_turnout]

# print(high_turnout_df)

# filtering columns using other columns
too_close = election['margin']<1

election.loc[too_close, 'winner'] = np.nan

# print(election)

# FILTERING USING NANS
titanic = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/titanic.csv')
df =titanic[['age', 'cabin']]
print(df.shape)

# dropna(how='all') drop columns w/ 0 values
print(df.dropna(how='all').shape)
# dropna(how='any') select columns w/ any non-0
print(df.dropna(how='any').shape)

# drop columns with less than 1000 non-missing values
print(titanic.dropna(thresh=1000, axis='columns').info())
