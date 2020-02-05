import pandas as pd
from scipy.stats import zscore

gapminder = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/gapminder_tidy.csv', index_col='Country')

# print(gapminder.head())

gapminder_2010 = gapminder[gapminder['Year']==2010]
gapminder_2010.to_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/gapminder_2010.csv')

print(type(gapminder_2010))

standardised = gapminder_2010.groupby('region')['life', 'fertility'].transform(zscore)
print(standardised)

outliers = (standardised['life'] < -3) | (standardised ['fertility'] > 3)
gm_outliers = gapminder_2010.loc[outliers]
print(gm_outliers)
