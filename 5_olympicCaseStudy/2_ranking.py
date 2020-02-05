import pandas as pd
medals = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/all_medalists.csv')

# country_names = medals['NOC']
#
# medal_counts = country_names.value_counts()
# print(medal_counts.head(15))
#
# # count medal by type: gold, silver, bronze
# # use .pivot_table() because we need to aggregate values by types
# counted = medals.pivot_table(index='NOC',values='Athlete', columns='Medal', aggfunc='count')
# print(counted)
#
# # create 'total' column
# counted['total'] = counted.sum(axis='columns') # NOTE: to sum across columns
# print(counted)
#
# # sort by total columns
# counted = counted.sort_values(by='total',ascending=False)
# # top 15 countries
# print(counted.head(15))
#
# # .drop_duplicates():
# # (Event_gender='W', Gender='Men') this should not exist
# ev_gen = medals[['Event_gender', 'Gender']]
# print(ev_gen)
# # find the odd combination
# ev_gen_uniques = ev_gen.drop_duplicates()
# print(ev_gen_uniques)
#
# # find possible errors with groupby
# medals_by_gender_count = medals.groupby(['Event_gender', 'Gender']).count()
# # print(medals_by_gender_count)
#
# # locate suspicous data
# sus = (medals['Event_gender']=='W') & (medals['Gender']=='Men')
# suspect = medals[sus]
# print(suspect)
#
# # use nunique() to rank by distinct sport
#
# country_grouped = medals.groupby('NOC')
# print(country_grouped)
# # compute No of distinct sports
# Nsports = country_grouped['Sport'].nunique()
# print(Nsports)
# Nsports.sort_values(ascending=False) # NOTE: no need for argument 'by'
# print(Nsports.head(15))
#
# # compare USA and USSR during the Cold War
# # create boolean to find 'Edition' between 1952 and 1988: during_cold_war
# during_cold_war = (medals['Edition'] >= 1952) & (medals['Edition'] <= 1988)
# # check if country is either USA or USSR
# is_usa_urs = medals['NOC'].isin(['USA', 'URS'])
# # create new df from 2 arguments above
# cold_war_medal = medals.loc[during_cold_war & is_usa_urs]
#
# country_grouped = cold_war_medal.groupby('NOC')
# Nsports = country_grouped['Sport'].nunique().sort_values(ascending=False)
# print(Nsports)

# counting USA and USSR Cold War Medals
medals_won_by_country = medals.pivot_table(index='Edition', columns='NOC', values='Athlete', aggfunc='count')
print(medals_won_by_country.head())
#slice medals_won_by_country
cold_war_usa_urs_medals = medals_won_by_country.loc['1952':'1988', ['USA', 'URS']]
print(cold_war_usa_urs_medals)
# create most_medal by applying .idmax()
most_medals = cold_war_usa_urs_medals.idxmax(axis='columns')
print(most_medals.value_counts())
