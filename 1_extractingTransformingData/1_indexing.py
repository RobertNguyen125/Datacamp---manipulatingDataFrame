import pandas as pd

sales = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/sales.csv', index_col='month')
print(sales)

# indexing by brackets

print(sales['salt']['Jan'])

#column attribute and row/using dot notations
print(sales.eggs['Mar']) # NOTE: column-row

# .loc access
print(sales.loc['May', 'spam']) #row-column

#.iloc access
print(sales.iloc[4,2]) # NOTE: row-column

#select only some columns
print(sales[['eggs', 'salt']])
