import pandas as pd

weather = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/weather.csv')

print(weather.columns)

def to_celsius(F):
    return 5/9*(F-32)

# weather_celsius = weather[['Mean TemperatureF', 'Mean Dew PointF']].apply(to_celsius)
# print(weather_celsius)
#
# # change the columns name
# weather_celsius.columns = ['Mean TemperatureC', 'Mean Dew PointC']
# print(weather_celsius)

election = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/pennsylvania2012_turnout.csv', index_col='county')

red_vs_blue = {'Obama': 'blue', 'Romney': 'red'}
election['color'] = election['winner'].map(red_vs_blue)

# vectorised functions
from scipy.stats import zscore

turnout_zscore = zscore(election['turnout'])

print(type(turnout_zscore))

election['turnout_zscore'] = turnout_zscore
print(election.head())
