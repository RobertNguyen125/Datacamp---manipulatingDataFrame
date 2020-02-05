import pandas as pd

titanic = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/titanic.csv')

print(titanic.head())

# .groupby(): single columns
by_class = titanic.groupby('pclass')
print(by_class)

count_by_class = by_class['survived'].count()
print(count_by_class)

# .groupby(): multiple columns
by_mult = titanic.groupby(['embarked', 'pclass'])
count_mult = by_mult['survived'].count()
print(count_mult)
