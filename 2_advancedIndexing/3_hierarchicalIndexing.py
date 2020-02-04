import pandas as pd

sales = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/2_3sales2.csv')
# print(sales)
# print(sales.loc[['CA', 'TX']])
# print(sales['CA':'TX'])

sales = sales.set_index(['state', 'month'])
sales = sales.sort_index()
# print(sales)

# NOTE: need to set and sort index before all these fancy indexing 
# # using .loc with nonunique indexes
# sales2 = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/2_3sales2.csv')
# sales2 = sales2.set_index(['state'])
# print(sales2)
# print(sales2.loc['NY'])

# index  multilevel of a MiltiIndex
# slice(None) in slicing parameter for the outermost dimension instead of ':'
# e.g: stocks.loc[(slice(None), slice('2016-10-03', '2016-10-04')), :]

NY_month1 = sales.loc[('NY',1)]
print(NY_month1)

# CA,TX data in month2
CA_TX_month2 = sales.loc[(['CA','TX'],2),:]
print(CA_TX_month2)

#access the inner month index and data for all states in month2
all_month2 = sales.loc[(slice(None),2),:]
print(all_month2)
