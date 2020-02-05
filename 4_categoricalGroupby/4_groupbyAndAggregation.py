import pandas as pd
sales = pd.DataFrame(
    {
        'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
        'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
        'bread': [139, 237, 326, 456],
        'butter': [20, 45, 70, 98]
    }
)

print(sales)

print(sales.groupby('city')[['bread', 'butter']].max())

#multi aggregation
print(sales.groupby('city')[['bread', 'butter']].agg(['max','sum']))

# custom aggregation
def data_range(series):
    return series.max() - series.min()

print(sales.groupby('city')[['bread', 'butter']].agg(data_range))

customers = pd.Series(['Dave', 'Alice', 'Bob', 'Alice'])

# custom aggregation: dictionaries

print(sales.groupby(customers)[['bread','butter']].agg({'bread':sum, 'butter':data_range}))
