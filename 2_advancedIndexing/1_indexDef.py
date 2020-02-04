'''pandas data structure
- indexes: sequence of labels | Immutable | homogenous
-  series: 1D array with index
- DataFrame: 2D array with Series as columns'''

import pandas as pd

# creating a Series

prices = [10.70, 10.86, 10.74, 10.71, 10.79]
days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
shares = pd.Series(prices, index=days)
shares.index.name = 'weekday'


print(shares)
print(shares.index)
print(shares.index[2])
print(shares.index[:2])
print(shares.index[-2:]) # NOTE: from the 2nd last index to tge last index
shares.index[2] = 'Wednesday' # NOTE: will raise an errors
