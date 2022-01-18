'''
merge_ordered()

Default method is outer join

pd.merge_ordered(df_1, df_2)

pd.merge_ordered(df_1, df_2, on = 'variable_that_will_provide_order')

pd.merge_ordered(df_1, df_2, on = 'variable_that_will_provide_order',
fill_method = 'ffill') ##Will fill  missing with the last non-missing value

'''


'''
merge as_of()

Similar to merge_ordered, but will match on nearest key column and not exact matches

pd.merge_asof(df1, df2, on = ['list_of_merges'],suffixes = ('_suffix_1','_suffix_2'))


it can be understood as a fuzzy join. Values will be matched based on how close they are to the right table
Value closer that is less than the left table

pd.merge_asof(df1, df2, on = ['list_of_merges'],suffixes = ('_suffix_1','_suffix_2'),direction = 'forward')
##Value closer that is greater than the left table


pd.merge_asof(df1, df2, on = ['list_of_merges'],suffixes = ('_suffix_1','_suffix_2'),direction = 'nearest')
##Value closer to the left table in absolute value


When to use:

Data sampled from a process
Developing a time-series training set
'''

'''
Selecting data with  .query()

- Use a query to select data. the string is after the WHERE clause would be.
- Use double quotes to select strings within the query

'''

'''
.melt Method: Pivoting from wide to long format. Changing the format of our dataset

data_frame.melt(id_vars = ['list_of_variables_that_will_be_kept'],value_vars = ['list_of_variables_that_will_be_unpivoted'],
var_name = 'name_of_the_unpivoted_variable',value_name = 'name_of_the_value_variable')


'''