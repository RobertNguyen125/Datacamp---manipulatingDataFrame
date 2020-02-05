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

# count all the sales on Sunday
print(sales.loc[sales['weekday'] == 'Sun'].count())

# .groupby() and .count()
print(sales.groupby('weekday').count())

# split-apply-combine

#.groupby() and aggregation
# .groupby(): single column
print(sales.groupby('weekday')['bread'].sum())
# .groupby(): multiple columns
print(sales.groupby('weekday')[['bread', 'butter']].sum())
# .groupby() and multiplevel index
print(sales.groupby(['city','weekday']).mean())

customers = pd.Series(['Dave', 'Alice', 'Bob', 'Alice'])
print(customers)
# NOTE: since 'customers' has the same index as 'sales' we can use .groupby('customers')

print(sales.groupby(customers)['bread'].sum()) # NOTE: customers w/o ''

# categorical data
print(sales['weekday'].unique())
sales['weekday'] = sales['weekday'].astype('category')
print(sales['weekday'])
