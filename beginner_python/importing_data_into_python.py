'''
Importing data into Pyhon

Plain text files

filename = 'file_name.txt'
file = open(filename, mode = 'r') #mode = 'w' is
text = file.read()
file.close() ##close the connection

Context manager with
with open('file.txt','r') as file:
	do something
'''
--------------------------------------------------------------------------------
'''
Code 1: Importing text
'''

# Open a file: file
file = open('moby_dick.txt', mode ='r')

# Print it
print(file.read()) ##Remember to use the .read() method

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)

--------------------------------------------------------------------------------
'''
Code 2: Line by line importing

With statements are useful to prevent opening and closing file connections
you can bind a variable file by using a context manager construct:
	with open('huck_finn.txt') as file
'''
# Read & print the first 3 lines
with open('moby_dick.txt') as file: ##this createt
    print(file.readline())
    print(file.readline())
    print(file.readline())

--------------------------------------------------------------------------------
'''
Code 3: Flat files (text files containing records)

np.loadtxt(filename, delimiter = '', skiprows = , usecols =[],dtype)
'''

# Import package
import numpy as np

# Assign filename to variable: file
file = 'digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',') ##Reading a csv using np loadtxt

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

--------------------------------------------------------------------------------
'''
Code 4: Flat files using numpy

'''

# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2]) ##skip rows refer to the total number of rows to skip
													#[0,2] means: only use first and third columns
# Print data
print(data)


--------------------------------------------------------------------------------
'''
Code 5: Importing flat file using numpy loadtx. Changing the data type and skipping rows

'''

# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()


--------------------------------------------------------------------------------
'''
Code 6: Using np.recfromcsv
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)

'''

# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])

--------------------------------------------------------------------------------
'''
Code 7: Flat files using pandas
A data frame has observations and variables
pd.read_csv()
'''

# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())

--------------------------------------------------------------------------------
'''
Code 8: Flat files using pandas

'''
# Assign the filename: file
file = 'digits.csv'

# Delimit the number of rows to pull (first five) and tells pandas that there is no header
data = pd.read_csv(file, nrows = 5, header =None)

# Build a numpy array from the DataFrame: data_array
data_array = np.array(data)

# Print the datatype of data_array to the shell
print(type(data_array))

--------------------------------------------------------------------------------
'''
Code 9: Customizing data import from a flat file
'''

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt'

# Set a new delimiter, defines a new na value, and tells to ignore data after '#'
data = pd.read_csv(file, sep='\t', comment="#", na_values='Nothing')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

--------------------------------------------------------------------------------
'''
Code 10: Loading a pickled file
import pickle
with open('pickled_fruit.pkl', 'rb') as file: ##'rb' means read-only for binary
	data = pickle.load(file)
print(data)
'''
# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))

--------------------------------------------------------------------------------
'''
Code 11: Getting excel sheet names and then reading files by sheet index or sheet name

Use pd.ExcelFile(file_name) to load the data into pandas and then load sheets accordingly
'''
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())

--------------------------------------------------------------------------------
'''
Code 12: Customizing an excel import
skiprows: how many rows do you want to skip?
names: list of strings containing variable names
usecols: which columns do you want to use (0-indexed)
'''

# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[1], names=['Country','AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[1], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())

--------------------------------------------------------------------------------
'''
Code 13: Importing SAS files
'''

# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas. Notice the use of a context manager
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

--------------------------------------------------------------------------------
'''
Code 14: Importing Stata files
'''

# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()

--------------------------------------------------------------------------------
'''
Code 15: Importing HDF5 files
'''


# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)

--------------------------------------------------------------------------------
'''
Code 16: Subsetting an HDF5 file
'''

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

--------------------------------------------------------------------------------
'''
Code 17: Load Matlab files and access values
'''
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))

# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))


# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()


--------------------------------------------------------------------------------
'''
Code 18: Creating a database engine and finding the tables in the schema

SQLAlchemy
'''
# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite') ##connection string to the SQLite database Chinook.sqlite

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)


--------------------------------------------------------------------------------
'''
Code 19: Connecting and querying the database

con = engine.connect() ##Connect to the db
rs = con.execute("SELECT ...") ## Pass a query to the database
df = pd.DataFrame(rs.fetchall()) ##save the result to a dataframe rs.fetchmany(size = 5) -> only 5 rows to import
df.columns = rs.keys() ##Fix variable names, if needed	
con.close() ##Closes the connection

with engine.connect() as con: ##Use constructs to open and close files
	do_something
'''
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute("SELECT * FROM Album")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())


--------------------------------------------------------------------------------
'''
Code 20: Using a WHERE clause
'''

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT * From Employee WHERE EmployeeId >=6")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())


--------------------------------------------------------------------------------
'''
Code 21: Querying directly with pandas
df = pd.read_sql_query("query here", engine)
'''

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Album", engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))

--------------------------------------------------------------------------------
'''
Code 22: Table relations

'''
