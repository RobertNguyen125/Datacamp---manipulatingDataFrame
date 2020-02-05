import pandas as pd

titanic = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/titanic.csv')
print(titanic.head())

by_sex_class = titanic.groupby(['sex','pclass'])

def impute_median(series):
    return series.fillna(series.median())

titanic['age'] = by_sex_class['age'].transform(impute_median)

print(titanic.tail(10))
