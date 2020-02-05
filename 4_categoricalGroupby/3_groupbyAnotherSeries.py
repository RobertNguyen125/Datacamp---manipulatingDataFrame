import pandas as pd

life = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/life_expectancy.csv', index_col='Country')
print(life.head())

regions = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/regions.csv', index_col='Country')
print(regions)

life_by_region = life.groupby(regions['region'])
print(life_by_region['2010'].mean())
