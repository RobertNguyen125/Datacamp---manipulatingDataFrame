import pandas as pd
import matplotlib.pyplot as plt

medals = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/all_medalists.csv')

# categorise order of medal to be consistent as: Broze < Silver < Gold
medals['Medal'] = pd.Categorical(values=medals['Medal'], categories=['Bronze', 'Silver', 'Gold'], ordered=True)

# create dataframe 'usa' with only U.S data
usa = medals[medals['NOC']=='USA']
print(usa.head())
# usa_medals_by_year = usa.pivot_table(index=['Edition', 'Medal'], values='Athlete', aggfunc='count')
# print(usa_medals_by_year)
# usa_medals_by_year =usa_medals_by_year.unstack(level='Medal')
# print(usa_medals_by_year)
usa_medals_by_year1 = usa.groupby(['Edition', 'Medal'])['Athlete'].count()
print(usa_medals_by_year1)
usa_medals_by_year1 = usa_medals_by_year1.unstack(level='Medal')
print(usa_medals_by_year1)

usa_medals_by_year1.plot()
# plt.savefig('/Users/apple/desktop/manipulatingDataFrames/5_olympicCaseStudy/USA_LinePlot.png')
# plt.show()

usa_medals_by_year1.plot.area()
plt.savefig('/Users/apple/desktop/manipulatingDataFrames/5_olympicCaseStudy/USA_areaPlot.png')
plt.show()
