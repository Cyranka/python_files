'''
Interesting code
'''


nobel['usa_born_winner'] = (nobel['birth_country'] == "United States of America") ##Creating a column of booleans
prop_usa_winners = nobel.groupby('decade',as_index = False)['usa_born_winner'].mean() ##Grouped mean



nobel['decade'] = (round(nobel['year']/10)*10).astype('int') ##Rounding to nearest decade

nobel.groupby("full_name").filter(lambda x: len(x) > 1) ##Filtering where appearances is greater than 1

# Converting birth_date from String to datetime
nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])

# Calculating the age of Nobel Prize winners
nobel['age'] = nobel['year'] - nobel['birth_date'].dt.year

sns.lmplot(x='year', y='age', data=nobel, lowess=True, 
           aspect=2, line_kws={'color' : 'black'}) ##Adding Lowess