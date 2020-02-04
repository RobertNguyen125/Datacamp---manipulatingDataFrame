# 1. use pandas native function
# 2. using numpy ufuncs ('Universal Functions') to transform entire columns 'elementwise'

import pandas as pd
import numpy as np

sales = sales = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/sales.csv', index_col='month')

# # df vectorised method
# print(sales.floordiv(12)) # NOTE: convert the whole df to dozen unit (round down)

# # np vectorised func
# print(np.floor_divide(sales,12))

# custom func
def dozen(n):
    return n/12

# print(sales.apply(dozen))
# print(sales.apply(lambda x: x //12))

# storing transformation: since the original df wont be changed
# create new column to store new computation

sales['dozen_of_eggs'] = sales['eggs'].floordiv(12)
# print(sales)

# working w/ string value
sales.index = sales.index.str.upper()
print(sales.index)
sales.index = sales.index.map(str.lower) # NOTE: different syntax

# defining  columns using  other columns
sales['salty_eggs'] = sales['salt'] + sales['dozen_of_eggs']
print(sales)
