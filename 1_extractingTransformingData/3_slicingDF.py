import pandas as pd
sales = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/sales.csv', index_col='month')

print(sales['eggs'])

# slicing  and indexing a Series
print(sales['eggs'][1:4]) # NOTE: [1:4] part of the eggs columns
print(sales['eggs'][4]) # NOTE: values associated with May

# .loc()
print(sales.loc[:,'eggs':'salt']) # NOTE: all rows, some columns
print(sales.loc['Jan':'Apr',:]) # NOTE: some rows, all columns
print(sales.loc['Mar':'May','salt':'spam']) # NOTE: some rows, some columns

# .iloc(): similar to loc, but use positional integer instead
print(sales.iloc[2:5,1:]) # NOTE: row 2-4, columns 1 to the rest

# use lists

print(sales.loc['Jan':'May', ['eggs','spam']]) # NOTE: the list will select certain columns/rows

# series vs 1-column DataFrame
sales['eggs'] # a series  by column name
sales[['eggs']] # a df w/ single column 
