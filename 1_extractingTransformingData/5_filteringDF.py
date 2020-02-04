import pandas as pd
sales = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/sales.csv', index_col='month')

# filter w boolean series
# print(sales.salt > 60)
# print(sales[sales.salt>60])# NOTE: df[df.columns]
#
# enough_salt_sold = sales.salt > 60
# print(sales[enough_salt_sold])

# combining filter
print(sales[(sales.salt > 50) & (sales.eggs < 200)]) # NOTE: & = and
print(sales[(sales.salt >= 50) | (sales.eggs < 200)]) # NOTE: | = or

# DataFrame with NaN and zeros
sales2 =sales.copy()
sales2['bacon'] = [0,0,50,60,70,80]
print(sales2)
