import pandas as pd
gapminder = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/gapminder_tidy.csv', index_col=['Year', 'region', 'Country']).sort_index()

print(gapminder.head())

by_year_region = gapminder.groupby(['Year', 'region'])

def spread(series):
    return series.max() - series.min()

aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

aggregated = by_year_region.agg(aggregator)

print(aggregated.tail(6))
