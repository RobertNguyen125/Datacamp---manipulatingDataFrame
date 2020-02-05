import pandas as pd

titanic = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/titanic.csv')

by_class = titanic.groupby('pclass')
by_class_sub = by_class[['age','fare']]
aggregated = by_class_sub.agg(['max', 'median'])

# use .loc to print all rows, and columns for [age, max]
print(aggregated.loc[:, ('age', 'max')])

# use .loc to print all rows, and columns for [fare, median]
print(aggregated.loc[:, ('fare', 'median')])
