import pandas as pd

users = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/users.csv', index_col=0)
users.set_index('weekday')
print(users)

# create new df w/o signup columns
users = users[['weekday','city','visitors']]
print(users)

# pivot df to match the df provided by datacamp,
users_pivot = users.pivot(index='weekday', columns='city', values='visitors')
print(users_pivot)

# users_pivot.to_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/3_6users.csv')

visitors_by_city_weekday = users_pivot.reset_index()
print(visitors_by_city_weekday)

visitors = visitors_by_city_weekday.melt(id_vars='weekday', value_name='visitors')
print(visitors)

# making data wide and long
users = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/users.csv', index_col=0)
users.set_index('weekday')
print(users)

skinny = pd.melt(users, id_vars = ['weekday', 'city'])
print(skinny)
