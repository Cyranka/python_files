'''
Cleaning data in Python

Common data problems
'''

'''
Code 1: Removing dollar sign from string and converting to integer
sales is a dataframe
'''

# str.strip() remove spaces at the beginning and at the end of the string:
sales['Revenue'] = sales['Revenue'].str.strip('$') ##Remove dollar sign

sales['Revenue'] = sales['Revenue'].astype('int') ##Cast as integer

assert sales['Revenue'].dtype == "int" ##assert that the revenue is an integer

'''
Code 2: Basic converting workflow
'''
# Print the information of ride_sharing
print(ride_sharing.info()) ##method prints information about a DataFrame including the index dtype and column dtypes,
							#non-null values and memory usage

# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())

# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category') ##Similar to factors in R

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'

# Print new summary statistics 
print(ride_sharing['user_type_cat'].describe())


'''
Code 3: Basic type conversion workflow example 2
'''

# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())

'''
Data range constraints

* Drop values
* Set custom minimums and maximums
* Impute missing
* Assign custom values

#Drop using filtering
movies = movies[movies['avg_rating']<=5]

#Drop using .drop
movies.drop(movies[movies['avg_rating']>5].index, inplace = True) ##Row indices where the condition is true

#Imposing limits. Loc can be used to filter and to change values
movies.loc[movies['avg_rating']>5,'avg_rating'] = 5 

##
today_date = dt.date.today()

'''

'''
Code 3: Converting and setting upper bounds to two different variables (one date, and one string)

'''
# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27: Make sure the subsetting is correct
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27 

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())


# Convert ride_date to datetime
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date'])

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())

'''
Uniqueness constraints

duplicated_rows = height_weight.duplicated() ##Creates a boolean series
print(duplicates)
height_weight[duplicates] ##this will slice the indices where the duplicates are

column_names = ['first_name', 'last_name','address']

##subset = only search for dups in these columns; keep = 'first' #mark duplicates as True except for the first
												  keep = 'last' #mark duplicates as True except for the last
												  keep = False #mark all duplicates as True
duplicates = height_weight.duplicated(subset= column_names, keep = False)


drop_duplicates() method
height_weight.drop_duplicates(inplace = True) ##Doesn't create a new object

##another way to treat duplicated inputs is to group the data and then average, or take the max, etc.
column_names = ['first_name', 'last_name', 'address']
summaries = {'height': 'max', 'weight': 'mean'} ##important dictionary
height_weight = height_weight.groupby(by = column_names).agg(summaries).reset_index()

'''

# Find duplicates
duplicates = ride_sharing.duplicated('ride_id', keep = False) ##Mark all duplicates as True

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id') ##Subset all duplicates

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']]) ##Show all duplicated rows


'''
#Using the set method to get uniques and running the difference method to find the errors
inconsistent_categories = set(study_data['blood_type']).difference(categories['blood_type'])
inconsistent_rows = study_data['blood_type'].isin(inconsistent_categories)
study_data[inconsistent_rows]
'''

'''
Code 4: Finding inconsistent categories and subsetting the data frame
'''

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows]) ##Notice the ~ symbol, meaning negation


'''
Categorical Variables
capitalization: df['column'].str.upper()
lowercase: df['column'].str.lower()
removing leading and trailing spaces: df['column'].str.strip()

Collapsing data into categories:

*using qcut()

group_names = ['x_1', 'x_2','x_3']
pd.qcut(df['column'], q = 3, labels = group_names) ##this is discretizetion based on data quantiles

*using cut(), creating category ranges and names

ranges = [0,200000,500000,np.inf] ##
group_names = ['0-200K', '200K-500K','500K+'] ##The first and last are the bounds, then the middle define cuts
pd.cut(df['column'], bins = ranges, labels = group_names)

#Replacing values in categories with others

#You need to pass a dictionary that maps an old value into a new one
mapping = {'Microsoft': 'DesktopOS','MacOS':'DesktopOS','Linux': 'DesktopOS','IOS': 'MobileOS', 'Android':'MobileOS'}

devices['operating_system'] = devices['operating_system'].replace(mapping)


'''


'''
Code 5: Changing capitalization and replacing values using a dictionary
'''
# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()

'''
Code 6: Using pd.cut with predefined ranges and labels, and another instance of replace
'''

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'],
                                bins = label_ranges, 
                                labels = label_names)

# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
            'Thursday': 'weekday', 'Friday': 'weekday', 
            'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)

'''
Cleaning text data

phones['Phone number'].str.replace("string_to_replace", "string_replacement")

digits = phones['Phone number'].str.len()
phones.loc[digits<10, "Phone number"] = np.nan ##replace with null

str.contains().any()
'''


'''
Code 7: Replacing strings in columns
'''

# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")


'''
Code 8:Filtering by string length
'''

# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])


'''
Uniformity
pd.to_datetime(birthdays['Birthday'],
			   infer_datetime_format = True, ##Attempt to infer format of each date
			   errors ='coerce') ##Return nas for places where converrsion failed
df['colummn'].dt.strftime("some_date_format")

'''

'''
Code 9: Subset for target rows, replace them, and ensure uniformity

'''
# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'


# Print the header of account_opened
print(banking['account_opened'].head())


'''
Code 10: Fixing dates

'''
# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 

# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y') ##Extract date

# Print acct_year
print(banking['acct_year'])

'''
Code 11
Cross field validation: the use of multiple fields in a dataset to sanity check data integrity
'''

# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where fund_columns row sum == inv_amount -> Doing rowwise sum
inv_equ = banking[fund_columns].sum(axis = 1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])

###Fix date column
# Store today's date and find ages
today = dt.date.today()
ages_manual = today.year - banking['birth_date'].dt.year

# Find rows where age column == ages_manual
age_equ = banking['age'] == ages_manual

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])

'''
Completeness: Code 12

df.isna().sum() ##Total Nas in the dataframe

import missingno as msno
import matplotlib.pyplot as plt
msno.matrix(airquality)

##Filtering for na rows
missing = airquality[airquality['CO2'].isna()]
completet = airquality[~airquality['CO2'].isna()]

df.dropna(subset = ['list_of_columns_to_drop_if_missing'])

##Replacing with metrics
co2_mean = airquality['CO2'].mean()
airquality_imputed = airquality.fillna({'CO2':co2_mean})
airquality_imputed.head()

'''

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

# Sort banking by age and visualize
banking_sorted = banking.sort_values('age')
msno.matrix(banking_sorted)
plt.show()



###Imputation
# Drop missing values of cust_id
banking_fullid = banking.dropna(subset = ['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount']*5

# Impute missing acct_amount with corresponding acct_imp
# If missing, replace with the value in the column, else keep the value
banking_imputed = banking_fullid.fillna({'acct_amount':acct_imp}) 
print(banking_imputed)

# Print number of missing values
print(banking_imputed.isna().sum())

'''
String similarity: Least possible amount of steps needed to transition from one string to another

from fuzzywuzzy import fuzz
fuzz.WRatio('Reeding', 'Reading') [0-100 based on how similar two strings are]

from fuzzywuzzy import fuzz

##Define string and array of possible matches
string = "Houston Rockets vs Los Angeles Lakers"
choices = pd.Series(['list_of_possible_matches'])
process.extract(string, choices, limit = 2) ## returns the closes strings

''' 

'''
Code 13: Checking basic strings against an array of strings
'''

# Import process from fuzzywuzzy
from fuzzywuzzy import process

# Store the unique values of cuisine_type in unique_types
unique_types = restaurants['cuisine_type'].unique()

# Calculate similarity of 'asian' to all values of unique_types
print(process.extract('asian', unique_types, limit = len(unique_types)))

# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit = len(unique_types)))

# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit = len(unique_types)))

# Similarity to all entries in the data frame
matches = process.extract('italian',restaurants['cuisine_type'],
limit = restaurants['cuisine_type'].shape[0])

# Inspect the first 5 matches
print(matches[0:5])

##In place changing using fuzzy match
# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

# Iterate through the list of matches to italian
for match in matches:
  # Check whether the similarity score is greater than or equal to 80
  if match[1] >=80:
    # Select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
    restaurants.loc[restaurants['cuisine_type'] == match[0],"cuisine_type"] = "italian"


# Iterate through a list of categories
for cuisine in categories:  
  # Create a list of matches, comparing cuisine with the cuisine_type column
  matches = process.extract(cuisine, restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

  # Iterate through the list of matches
  for match in matches:
     # Check whether the similarity score is greater than or equal to 80
    if match[1] >= 80:
      # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
      restaurants.loc[restaurants['cuisine_type'] == match[0]] = cuisine
      
# Inspect the final result
print(restaurants['cuisine_type'].unique())    


'''
Generating Pairs

import recordLinkage

##make sure that your records have an index and are sorted correctly

indexer = recordlinkage.Index() ##creates indexing object

#Generate pairs blocked on state
indexer.block('state')
pairs = indexer.index(census_A, census_B)

#Create a compare object
compare_cl = recordlinkage.Compare()

##Find exact matches for pairs of date_of_birth and state
compare_cl.exact('date_of_birth', 'date_of_birth', label = 'date_of_birth')
compare_cl.exact('state', 'state', label = 'state')

##Find similar matches for pairs of surname and address_1 using string similarity
compare_cl.string('surname', 'surname', threshold = 0.85,label ='surname')
compare_cl.string('address_1', 'address_2', threshold = 0.85,label ='address_1')

#find matches
potential_matches = compare_cl.compute(pairs, census_A, census_B)

##Find potential matches
potential_matches[potential_matches.sum(axis = 1)=>2]


'''


'''
Record Linkage

potential_matches[potential_matches.sum(axis = 1)=>2] ##Returns possible duplicate records

##Extract only indices from the second column
duplicate_rows = matches.index.get_level_values(1) ##1 is to return matching indices for the rows

census_B_duplicates = census_B[census_B.index.isin(duplicatee_rows)]
census_B_new = census_B[~census_B.index.isin(duplicatee_rows)]

full_census = census_A.append(census_B_new)
'''