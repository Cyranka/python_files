'''
Dataset introduction

* Each row represents a single traffic stop
* df.isnull #Returns a dataframe of boolean values (True if missing)
* df.isnull().sum() ##Total missing valuues
* df.drop(['list_of_columns_to_drop'], axis = 'columns') ##drop columns
* df.dropna() ##Drop rows with missing values
'''

'''
Code 1: Loading, counting NAs, and dropping columns
'''

# Import the pandas library as pd
import pandas as pd

# Read 'police.csv' into a DataFrame named ri
ri = pd.read_csv('police.csv')

# Examine the head of the DataFrame
print(ri.head(5))

# Count the number of missing values in each column
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)

# Drop the 'county_name' and 'state' columns
ri.drop(['county_name', 'state'], axis='columns', inplace=True)

# Examine the shape of the DataFrame (again)
print(ri.shape)

'''
Code 2: Dropping rows with missing values
'''

# Count the number of missing values in each column
print(ri.isnull().sum())

# Drop all rows that are missing 'driver_gender'
ri.dropna(subset=['driver_gender'], inplace=True)

# Count the number of missing values in each column (again)
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)

'''
Using proper data types
df.dtypes #Returns a series with the data types for each column

df['column'] = df.column.astype('desired_type')
df['column'] = df['column'].astype('desired_type')
'''

'''
Code 3: Changing a column to boolean type
'''

# Examine the head of the 'is_arrested' column
print(ri.is_arrested.head())

# Change the data type of 'is_arrested' to 'bool'
ri['is_arrested'] = ri.is_arrested.astype('bool')

# Check the data type of 'is_arrested' 
print(ri.is_arrested.head())

'''
Creating a DateTimeIndex

combined = apple.date.str.cat(apple.time, sep = ' ') #Cat is short for concatenate
apple['date_and_time'] = pd.to_datetime(combined)
apple.set_index('column_to_set', inplace = True)

'''

'''
Code 4: Concatenating strings and setting an index
'''
# Concatenate 'stop_date' and 'stop_time' (separated by a space)
combined = ri.stop_date.str.cat(ri.stop_time, sep = ' ')

# Convert 'combined' to datetime format
ri['stop_datetime'] = pd.to_datetime(combined)

# Examine the data types of the DataFrame
print(ri.dtypes)

# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Examine the index
print(ri.index)

# Examine the columns
print(ri.columns)

'''
Counting unique values
.value_counts()
.value_counts().sum()	
'''

'''
Code 5: Subsetting DF for specific groups and computing counts
'''

# Create a DataFrame of female drivers
female = ri[ri['driver_gender'] == 'F']

# Create a DataFrame of male drivers
male = ri[ri['driver_gender'] == 'M']

# Compute the violations by female drivers (as proportions)
print(female.violation.value_counts(normalize = True))

# Compute the violations by male drivers (as proportions)
print(male.violation.value_counts(normalize = True))