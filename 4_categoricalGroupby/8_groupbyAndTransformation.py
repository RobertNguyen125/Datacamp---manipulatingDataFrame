import pandas as pd
auto = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/auto-mpg.csv')
print(auto.head())

def zscore(series):
    return (series - series.mean())/series.std()

# apply the score to the function
print(zscore(auto['mpg']).head()) # NOTE: there is 1 results > 1 std, need to normalise the data by year

# NOTE: .agg apply reduction func
# NOTE: .transform apply elementwise func
print(auto.groupby('yr')['mpg'].transform(zscore).head())

def zscore_with_year_and_name(group):
        df = pd.DataFrame(
        {'mpg': zscore(group['mpg']),
         'year': group['yr'],
         'name': group['name']}
        )
        return df

print(auto.groupby('yr').apply(zscore_with_year_and_name).head())
