import pandas as pd

auto = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/auto-mpg.csv')

print(auto.head())

print(auto.groupby('yr')['mpg'].mean())

# only want to know the mean for a type of car -> group before aggregating
# save the output of group before aggregating as: splitting
splitting = auto.groupby('yr')
print(type(splitting))

print(type(splitting.groups)) # NOTE: this is a dict()

print(splitting.groups.keys()) # NOTE: keys are the year and the corresponding rows is the year in the OG df

for group_name, group in splitting: # NOTE: this is like for k,v in dict
    avg = group['mpg'].mean()
    print(group_name, avg)

# include filter for chevrolet:
for group_name, group in splitting:
    avg = group.loc[group['name'].str.contains('chevrolet'), 'mpg'].mean()
    print(group_name, avg)

# dictionary comprehension: https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
# dict_variable = {k:v for (k,v) in dict.items()}

# keys are the year (group names) and the values are the filtered averages
chevy_means = {year:group.loc[group['name'].str.contains('chevrolet'), 'mpg'].mean()
                for year, group in splitting}
print(pd.Series(chevy_means))

# boolean groupby
chevy = auto['name'].str.contains('chevrolet')
print(auto.groupby(['yr', chevy])['mpg'].mean())
