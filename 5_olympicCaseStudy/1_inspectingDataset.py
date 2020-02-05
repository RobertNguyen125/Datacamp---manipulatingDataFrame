import pandas as pd
medals = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/all_medalists.csv')
# print(medals.columns)

# NOC: National Olympic Committee

USA_edition = medals.loc[medals['NOC']=='USA'].groupby('Edition')['Medal'].count()
print(USA_edition)
