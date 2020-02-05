import pandas as pd
sales = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/sales/sales-feb-2015.csv',
                    index_col='Date', parse_dates=True)

print(sales.head())

# group the sales  data by day of the week and aggregate teh sum of columns
# NOTE: check the strftime('%a')
print(sales.groupby(sales.index.strftime('%a'))['Units'].sum())
