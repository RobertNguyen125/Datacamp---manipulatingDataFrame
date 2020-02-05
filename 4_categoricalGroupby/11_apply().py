import pandas as pd

gapminder_2010 = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/gapminder_2010.csv')

def disparity(gr):
    # Compute the spread of gr['gdp']: s
    s = gr['gdp'].max() - gr['gdp'].min()
    # Compute the z-score of gr['gdp'] as (gr['gdp']-gr['gdp'].mean())/gr['gdp'].std(): z
    z = (gr['gdp'] - gr['gdp'].mean())/gr['gdp'].std()
    # Return a DataFrame with the inputs {'z(gdp)':z, 'regional spread(gdp)':s}
    return pd.DataFrame({'z(gdp)':z , 'regional spread(gdp)':s})

regional = gapminder_2010.groupby('region')
reg_disp = regional.apply(disparity)
# print(reg_disp.loc[['United States', 'United Kingdom', 'China']])
print(reg_disp.loc[['United States', 'United Kingdom', 'China']])
