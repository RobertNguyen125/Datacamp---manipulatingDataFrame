# .pivot() might not work with duplicated data so we use .pivot_table() instead
import pandas as pd
more_trials = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/trials_03.csv')
# print(more_trials)
#
# print(more_trials.pivot_table(index='treatment', columns='gender', values='response'))
# print(more_trials.pivot_table(index='treatment', columns='gender', values='response',aggfunc='count'))

users = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/users.csv',index_col=0)
by_city_day = users.pivot_table(index='weekday', columns='city')
print(by_city_day)

# using aggregation in .pivot_table()

count_by_weekday1 = users.pivot_table(index='weekday', aggfunc='count')
print(count_by_weekday1)

count_by_weekday2 = users.pivot_table(index='weekday', aggfunc=len)
print(count_by_weekday2)

# use margins in pivot tables: add total margin by useing margins=True in .pivot_table()
signup_and_visitors = users.pivot_table(index='weekday',aggfunc=sum)
print(signup_and_visitors)
signup_and_visitors_margin = signup_and_visitors.pivot_table(index='weekday', aggfunc=sum, margins=True)
print(signup_and_visitors_margin)
