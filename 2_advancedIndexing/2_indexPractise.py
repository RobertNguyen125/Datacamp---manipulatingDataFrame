import pandas as pd

sales = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/sales.csv', index_col='month')

new_idx = [i.upper() for i in sales.index]
sales.index= new_idx
sales.index.name = 'MONTHS'
sales.columns.name = 'PRODUCTS'
print(sales)

sales2 = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/sales.csv')
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales2.index = months
print(sales2)
