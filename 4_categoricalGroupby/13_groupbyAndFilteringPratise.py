import pandas as pd

# using .apply()
titanic = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/titanic.csv')
print(titanic.head())

# analyse the survival rates from 'C' deck, containing most passengers
# groupby('sex') then use apply

by_sex = titanic.groupby('sex')

def c_deck_survival(gr):
    c_passenger = gr['cabin'].str.startswith('C').fillna(False)
    return gr.loc[c_passenger, 'survived'].mean()
c_surv_by_sex = by_sex.apply(c_deck_survival)

print(c_surv_by_sex)

# using .filter()
# use Feb sales data and remove entries from companies that purchased <= 35 Units/month

sales = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/sales/sales-feb-2015.csv',
                    index_col='Date', parse_dates=True)
print(sales.head())

by_company = sales.groupby('Company')

by_com_sum = by_company['Units'].sum()
print(by_com_sum > 35)

by_com_filt = by_company.filter(lambda g:g['Units'].sum() > 35)
# print(by_com_filt)


# using .map() uing titanic dataset
# find out the survival rates of children < 10

under_10 = (titanic['age'] < 10).map({True:'Under 10', False:'Over 10'})
survived_mean_1 = titanic.groupby(under_10)['survived'].mean()
print(survived_mean_1)

survived_mean_2 = titanic.groupby([under_10, 'pclass'])['survived'].mean()
print(survived_mean_2)
