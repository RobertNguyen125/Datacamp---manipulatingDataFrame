import pandas as pd
users = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/users.csv', index_col=0)

print(users)

users = users.set_index(['city','weekday'])
# print(users)
users = users.sort_index()
# print(users)

byweekday = users.unstack(level=1)
# print(byweekday)

# print(byweekday.stack(level='weekday'))

# exercise 2:
bycity = users.unstack(level=0)
# print(bycity)

# print(bycity.stack(level='city'))

# restoring the index order
newusers = bycity.stack(level='city')
print(newusers)

newusers =newusers.swaplevel(0,1)
newusers = newusers.sort_index()
print(newusers)
