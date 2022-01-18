'''
Dates in python

* Python contains a special date class

#import date
from datetime import date
two_hurrricanes_dates = [date(2016,10,7)]
two_hurrricanes_dates[0].year
two_hurrricanes_dates[0].month
two_hurrricanes_dates[0].day
two_hurrricanes_dates[0].weekday() #returns an integer (0 is Monday,...,6 is Sunday)
'''

'''
Code 1: Creating a date object and extracting the weekday
'''

# Import date from datetime
from datetime import date

# Create a date object
hurricane_andrew = date(1992, 8, 24)

# Which day of the week is the date?
print(hurricane_andrew.weekday())

'''
Code 2
'''

# Counter for how many before June 1
early_hurricanes = 0

# We loop over the dates
for hurricane in florida_hurricane_dates:
  # Check if the month is before June (month number 6)
  if hurricane.month < 6:
    early_hurricanes = early_hurricanes + 1
    
print(early_hurricanes)

'''
Math with dates

from datetime import date
d1 = date(2017,11,5)
d2 = date(2017,12,4)
l = [d1,d2]
delta = d2 - d1 #Arithmetic with dates. Returns a time.delta objects	
print(delta.days)

from datetime import timedelta
td = timedelta(days = 29)
print(d1 + td) ##Adding a timedelta object to a date

'''


'''
Code 3: Basic time arithmetic
'''

# Import date
from datetime import date

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12, 13)

# Subtract the two dates and print the number of days
print((end - start).days)


'''
Code 4: Looping over a dictionary and using methods
'''

# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}

# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
  # Pull out the month
  month = hurricane.month
  # Increment the count in your dictionary by one
  hurricanes_each_month[month] +=1
  
print(hurricanes_each_month)

'''
Code 5: Using sorted() on a list of dates
dates_scrambled is an unsorted list of dataframes
'''

# Put the dates in order
dates_ordered = sorted(dates_scrambled)

# Print the first and last ordered dates
print(dates_ordered[0])
print(dates_ordered[-1])


'''
Turning dates into strings
* Python represents dates as YYYY-MM-DD
* Express date as a string in ISO format d.isoformat()
* To express it as another format d.strftime("pass a format string")

'''

'''
Code 6: Formatting dates
'''

# Assign the earliest date to first_date
first_date = sorted(florida_hurricane_dates)[0]

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

print("ISO: " + iso)
print("US: " + us)


'''
Dates and times: dttm
from datetime import datetime
dt = datetime(2017, 10,1,15,23,25) ## Y M D Hour Minute Seconds
dt = datetime(2017, 10,1,15,23,25,50000) ## Y M D Hour Minute Second Micro-second

#Replacing in dttm
dt_hr = dt.replace(minute = 0, second = 0, microsecond = 0)
'''

'''
Code 7: Replacing in datetime and displaying as iso()
'''

# Import datetime
from datetime import datetime

# Create a datetime object
dt = datetime(2017, 12, 31, 15, 19, 13)

# Replace the year with 1917
dt_old = dt.replace(year = 1917)

# Print the results in ISO 8601 format
print(dt_old)

'''
Code 8: placing a counter and inspecting date and time elements
'''
# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}
  
# Loop over all trips
for trip in onebike_datetimes:
  # Check to see if the trip starts before noon
  if trip['start'].hour < 12:
    # Increment the counter for before noon
    trip_counts['AM'] += 1
  else:
    # Increment the counter for after noon
    trip_counts['PM'] += 1
  
print(trip_counts)

'''
Printing and parsing datetimes
dt = datetime(2017, 12, 30, 15, 19,13)
print(dt.strftime("%Y-%m-%d %H:%M:%S")) ##How to print datetime
print(dt.strftime("%H:%M:%S on %d/%m/%Y")) ##Changing format

Parsing datetimes with strptime
from datetime import datetime

dt = datetime.strptime("string to parse","format the string is in") ##Requires exact matching

#Formatting from UNIX timestamp
ts = 1514665153
#Convert to datetime
print(datetime.fromtimestamp(ts))
 
'''

'''
Code 9: 
'''

# Import the datetime class
from datetime import datetime

# Starting string, in MM/DD/YYYY HH:MM:SS format
s = '12/15/1986 08:00:00'

# Write a format string to parse s: For parsing to be successful, the match needs to be exact
fmt = '%m/%d/%Y %H:%M:%S'

# Create a datetime object d
d = datetime.strptime(s, fmt)

# Print d
print(d)


'''
Code 10:  Using strptime. Also notice how to loop through a list of tuples
'''

# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []

# Loop over all trips
for (start, end) in onebike_datetime_strings:
  trip = {'start': datetime.strptime(start,fmt),
          'end': datetime.strptime(end, fmt)}
  
  # Append the trip
  onebike_datetimes.append(trip)

'''
Code 11

strptime means string parser, this will convert a string format to datetime.
strftime means string formatter, this will format a datetime object to string format
'''

# Import datetime
from datetime import datetime

# Pull out the start of the first trip
first_start = onebike_datetimes[0]['start']

# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"

# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))

'''
Code 12: Using timestamps
'''

# Import datetime
from datetime import datetime

# Starting timestamps
timestamps = [1514665153, 1514664543]

# Datetime objects
dts = []

# Loop
for ts in timestamps:
  dts.append(datetime.fromtimestamp(ts))
  
# Print results
print(dts)

'''
Code 13: Using timedelta
'''

# Initialize a list for all the trip durations
onebike_durations = []

for trip in onebike_datetimes:
  # Create a timedelta object corresponding to the length of the trip
  trip_duration = trip['end'] - trip['start']
  
  # Get the total elapsed seconds in trip_duration
  trip_length_seconds = trip_duration.total_seconds() ##Total seconds() is different from seconds
  
  # Append the results to our list
  onebike_durations.append(trip_length_seconds)


'''
UTC offsets
from datetime import datetime, timedelta, timezone

#Specify Timezone (EST in the example)
ET = timezone(timedelta(hours = -5))

#Timezone-aware datetime
dt = datetime(2017,12,30,15,9,3,tzinfo = ET)

#Change timezone
IST = timezone(timedelta(hours = 5, minutes = 30))

#Convert
print(dt.astimezone(IST))

'''

'''
Code 14: Setting UTC timezone without timedelta
'''

# Import datetime, timezone
from datetime import datetime, timezone

# October 1, 2017 at 15:26:26, UTC
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=timezone.utc)

# Print results
print(dt.isoformat())


'''
Code 15: Setting PST timezone using timezone(timedelta(hours = , minutes = ))
'''
# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone

# Create a timezone for Pacific Standard Time, or UTC-8
pst = timezone(timedelta(hours=-8)) ##This is with respect to Greenwich time

# October 1, 2017 at 15:26:26, UTC-8
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)

# Print results
print(dt.isoformat())

'''
Code 16: Setting up an Australian date time object
'''

# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone

# Create a timezone for Australian Eastern Daylight Time, or UTC+11
aedt = timezone(timedelta(hours = 11))

# October 1, 2017 at 15:26:26, UTC+11
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=aedt)

# Print results
print(dt.isoformat())


'''
Code 17: Replacing the tzinfo in a datetime object

'''
  # Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours = -4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo = edt)
  trip['end'] = trip['end'].replace(tzinfo = edt)

'''
Code 18: Comparing times
'''
# Loop over the trips
for trip in onebike_datetimes[:10]:
  # Pull out the start
  dt = trip['start']
  # Move dt to be in UTC
  dt = dt.astimezone(timezone.utc) #t
  
  # Print the start time in UTC
  print('Original:', trip['start'], '| UTC:', dt.isoformat())


'''
Time zone database
from datetime import datetime
from dateutil import tz

et = tz.gettz('America/New_York') #Continent/Major City


astimezone() ##Replaces THE CLOCK AND THE UTC OFFSET
replace(tzinfo = timezone.) #REPLACES ONLY THE UTC OFFSET, BUT NOT THE CLOCK
'''

'''
Code 19: Using the TZ Package
'''

# Import tz
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo = et)
  trip['end'] = trip['end'].replace(tzinfo = et)

'''
Code 20: Changing timezone on objects
'''

# Create the timezone object
sm = tz.gettz('Pacific/Apia')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in Samoa?
notlocal = local.astimezone(sm)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())


'''
Daylight savings time

from datetime import timezone, timedelta

EST = timezone(timedelta(hours = -5))
EDT = timezone(timedelta(hours = -4))
'''

'''
Code 21: Adjusting for daylight savings
'''

# Import datetime, timedelta, tz, timezone
from datetime import datetime, timedelta, timezone
from dateutil import tz

# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())

# How many hours have elapsed?
print((end - start).total_seconds()/(60*60))

# What if we move to UTC?
print((end.astimezone(timezone.utc) - start.astimezone(timezone.utc))
      .total_seconds()/(60*60))

'''
When in doubt, always use tz instead of hand-rolling timezones,
so it will catch the Daylight Saving rules (and rule changes!) for you
'''

'''
Ending daylight savings time
All needs to be mapped back to UTC. UTC is unambiguous

tz.datetime_ambiguous() ##Returns True/False if it is possible for the time to occurs in different timezones
tz.enfold
'''


'''
Code 22: finding ambiguous times in a list of tzs
'''
# Loop over trips
for trip in onebike_datetimes:
  # Rides with ambiguous start
  if tz.datetime_ambiguous(trip['start']):
    print("Ambiguous start at " + str(trip['start']))
  # Rides with ambiguous end
  if tz.datetime_ambiguous(trip['end']):
    print("Ambiguous end at " + str(trip['end']))


'''
Reading date and time data in Pandas

pd.read_csv("file_name", parse_dates = ["list_of_columns_to_convert_to_date"])

df['column'] = pd.to_datetime(df['column'], format = 'desired date format')

df['column'].dt.total_seconds().head( )

'''

'''
Code 23: Using parse_dates method in read_csv, and doing basic arithmetic on dates

'''
# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = [trip.total_seconds() for trip in ride_durations]

print(rides['Duration'].head())

'''
Summarizing datetime data in pandas

* you can pass functions to timedelta objects -> mean(), sum()

* also possible to do operations with other timedelta constructs:
  rides['duration'].sum()/timedelta(days = 91)

* groupby: rides.groupby('Member type')['Duration seconds'].mean()

* using resample method
rides.resample('M', on = 'Start date')['Duration seconds'].mean()
'''

'''
Code 24: Basic time calculation
'''

# Create joyrides
joyrides = (rides['Start station'] == rides['End station'])

# Total number of joyrides
print("{} rides were joyrides".format(joyrides.sum()))

# Median of all rides
print("The median duration overall was {:.2f} seconds"\
      .format(rides['Duration'].median()))

# Median of joyrides
print("The median duration for joyrides was {:.2f} seconds"\
      .format(rides[joyrides]['Duration'].median())) 


'''
Code 25: Using resampling and plotting the data
'''    
# Import matplotlib
import matplotlib.pyplot as plt

# Resample rides to daily, take the size, plot the results
rides.resample('D', on = 'Start date')\
  .size()\
  .plot(ylim = [0, 15])

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on = 'Start date')\
  .size()\
  .plot(ylim = [0, 150])


# Show the results
plt.show()

'''
Code 26: Using resampling and grouping by another variable
'''

# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M',on = 'Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())

'''
Code 27: Grouping by then resampling
'''

# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type')\
  .resample('M', on = 'Start date')

# Print the median duration for each group
print(grouped['Duration'].median())

'''
Additional date time methods in Pandas

- Date times, by themselves, are naive, because they don't take into account the timezone

- Adding a timezone to a Pandas column
rides['Start date'].dt.tz_localize('America/New York')

- If there is an ambiguous time
rides['Start date'].dt.tz_localize('America/New York', ambiguous = 'NaT') ##Not a Time

- Useful functions

df['column'].dt.year #Pulls year from date column
df['column'].dt.month #Pulls month from date column
df['column'].dt.weekday_name #Pulls weekday from date column

'''

'''
Code 28

dt.tzconvert() converts to a new timezone, whereas dt.tzlocalize() sets a timezone in the first place.

After localizing, you are forced to convert. trying to use tz_localisze will throw an error
'''

# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', 
                                             ambiguous='NaT')

# Print first value
print(rides['Start date'].iloc[0])

# Convert the Start date column to Europe/London
rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')

# Print the new value
print(rides['Start date'].iloc[0])

'''
Code 29: Using one of the dt methods and grouping by
'''

# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.weekday_name

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())


'''
Code 30: Using shift
Shift method is equal to lag() in R
'''

# Shift the index of the end date up one; now subract it from the start date
rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))

# Move from a timedelta to a number of seconds, which is easier to work with
rides['Time since'] = rides['Time since'].dt.total_seconds()

# Resample to the month
monthly = rides.resample('M', on = 'Start date')

# Print the average hours between rides each month
print(monthly['Time since'].mean()/(60*60))


####################################################################################################
'''
Extra code (EC)
'''

'''
EC 1: Generating all days between two dates
'''

#Method 1
from datetime import date
from datetime import timedelta

date_1 = date(2020,1,1)
date_2 = date(2020,12,31)


time_diff = (date_2 - date_1).days

list_of_dates = []

for i in range(0,time_diff):
    list_of_dates.append(date_1 + timedelta(days = i))


'''
EC 2: Summing a list
'''

# What was the total duration of all trips?
total_elapsed_time = sum(onebike_durations)

# What was the total number of trips?
number_of_trips = len(onebike_durations)
  
# Divide the total duration by the number of trips
print(total_elapsed_time / number_of_trips) ##gives the mean tripss

# Calculate shortest and longest trips
shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)
