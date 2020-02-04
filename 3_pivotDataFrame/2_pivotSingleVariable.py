import pandas as pd
users = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/users.csv', index_col=0)
print(users)

print(users.pivot(index='weekday',columns='city',values='visitors'))
signups_pivot = users.pivot(index='weekday', columns='city', values='signups')
print(signups_pivot)

# pitvot all variables
print(pivot)
