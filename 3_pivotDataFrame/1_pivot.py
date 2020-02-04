import pandas as pd

trials = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/trials_01.csv')
print(trials)

print(trials.pivot(index='treatment', columns = 'gender', values ='response'))
# index: pick columns to be the index
# columns: pick columns to be the columns label
# values: values inside each columns

print(trials.pivot(index='treatment',columns='gender'))
