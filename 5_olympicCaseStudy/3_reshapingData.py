import pandas as pd
import matplotlib.pyplot as plt
medals = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/all_medalists.csv')

# print(medals['Athlete'])
france = medals['NOC'] == 'FRA'
france_grps = medals[france].groupby(['Edition', 'Medal'])['Athlete'].count()
print(france_grps)

france_medal = france_grps.unstack()
print(france_medal)

france_medal.plot(kind='line', marker='.')
plt.title('France Medals')
plt.show()
