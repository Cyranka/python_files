#Pyplot interface

'''
* Code 1 (Simple line graph containing columns from ttwo different data frames):
'''
# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots() ##You can pass arguments defining the number of total plots (default is 1)

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["MONTH"],seattle_weather['MLY-PRCP-NORMAL'])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather["MONTH"],austin_weather['MLY-PRCP-NORMAL'])

# Call the show function
plt.show()
	
--------------------------------------------------------------------------------
'''
* Code 2 (Simple line graph but adding some customization)
'''
# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"],
color ='b', marker = 'o',linestyle = "--")

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"],
color ='r',marker = 'v',linestyle = "--")

# Customize the x-axis label
ax.set_xlabel('Time (months)')

# Customize the y-axis label
ax.set_ylabel('Precipitation (inches)')

# Add the title
ax.set_title('Precipitation (inches)')

# Call show to display the resulting plot
plt.show()

--------------------------------------------------------------------------------
'''
* Code 3 (Creating multiple plots/faceted plot)
'''

# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2) ##The first argument is number of rows, the second is number of columns

# Notice that each of the plots needs to be explicitly referenced in the ax[row_n,col_n] argument
# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather['MONTH'],seattle_weather['MLY-PRCP-NORMAL'])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1, 0].plot(austin_weather['MONTH'],austin_weather['MLY-PRCP-NORMAL'])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1, 1].plot(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'])
plt.show()


--------------------------------------------------------------------------------
'''
* Code 4 (Creating a plot that shares the y-axis)
'''

# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)


# Plot Seattle precipitation data in the top axes
##since there is only one column, there is no need to explicitly name the column
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'], color = 'b') ##since there is only one row, there is no need
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-25PCTL'], color = 'b', linestyle = "--")
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-75PCTL'], color = 'b', linestyle = "--")

# Plot Austin precipitation data in the bottom axes
##since there is only one column, there is no need to explicitly name the column
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'], color = 'r')
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-25PCTL'], color = 'r', linestyle = "--")
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-75PCTL'], color = 'r', linestyle = "--")
plt.show()


--------------------------------------------------------------------------------
'''
* Code 5 (Plotting Time series)
'''

# Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv',parse_dates = ['date'],
index_col = ['date']) ##This will parse the column 'date' as a datetime and will set it as an index

#plot the data
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index,climate_change["relative_temp"])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show() 

--------------------------------------------------------------------------------
'''
Code 6 (Using a twix() with Time Series Data)

If you want to plot two time-series variables that were recorded at the same times, you can add both of them to the same subplot.
If the variables have very different scales, you'll want to make sure that you plot them in different twin Axes objects. 
These objects can share one axis (for example, the time, or x-axis) while not sharing the other (the y-axis).


'''

import matplotlib.pyplot as plt

# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change['co2'], color='blue')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change['relative_temp'], color='red')

plt.show()

--------------------------------------------------------------------------------
'''
Code 7 (A function for plotting)
Notice that the axes is the variable we assined to the axes object


'''

# Define a function called plot_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)

##Using the function above
fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(axes = ax,x = climate_change.index, y =climate_change['co2'],
color = "blue", xlabel = 'Time (years)',ylabel  = 'CO2 levels')

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(axes = ax2,x = climate_change.index, y =climate_change['relative_temp'],
color = "red",
xlabel= 'Time (years)',ylabel = 'Relative temperature (Celsius)')

--------------------------------------------------------------------------------
'''
Code 8: Basic annotation

'''

fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index,climate_change['relative_temp'])

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate(text = '>1 degree',
xy = (pd.Timestamp('2015-10-06'), 1))

plt.show()

##Annotation example 2:
fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(axes = ax,x = climate_change.index, y =climate_change['co2'],
color = "blue", xlabel = 'Time (years)',ylabel  = 'CO2 levels')

# Create an Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(axes = ax2,x = climate_change.index, y =climate_change['relative_temp'],
color = "red",
xlabel= 'Time (years)',ylabel = 'Relative temp (Celsius)')


# Annotate point with relative temperature >1 degree
ax2.annotate(">1 degree", ##Annotation text
	xy = (pd.Timestamp('2015-10-06 00:00:00'),1), ##This controls the point we want to annotate
	xytext =(pd.Timestamp('2008-10-06 00:00:00'),-0.2), ##This controls where we are placing the annotation text
	arrowprops={'arrowstyle':'->','color': 'gray'}) ##Arrow properties

plt.show()

--------------------------------------------------------------------------------
'''
Code 9: Simple Bar Plot. Includes label rotations, tick modifications and axes names

The second argument for the ax.bar is 'height' and it could be a vector of means, for example
medals is a dataframe
'''

fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index,medals['Gold'])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation = 90)

# Set the y-axis label
ax.set_ylabel("Number of medals")

plt.show()
--------------------------------------------------------------------------------
'''
Code 10: Stacked Bar Chart. Notice the addition of legends and how to stack bars

medals is a dataframe

'''


# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals['Gold'], label='Gold')

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals['Silver'], bottom=medals['Gold'],
label = 'Silver')

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals['Bronze'],
bottom=medals['Gold'] + medals['Silver'],
label = 'Bronze')

# Display the legend
ax.legend() ##This tells python to display the legend (Generated automatically)

plt.show()

--------------------------------------------------------------------------------
'''
Code 11: Histograms

mens_rowing and mens_gymnastics are data frames

'''
fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel('Weight (kg)')

# Set the y-axis label to "# of observations"
ax.set_ylabel('# of observations')

plt.show()


--------------------------------------------------------------------------------
'''
Code 12: Histograms with customization of histogram type, labels, and bins

mens_rowing and mens_gymnastics are data frames

'''


fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'], label = "Rowing",
histtype = 'step',
bins = 5)

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'], label = "Gymnastics",
histtype = 'step',
bins = 5)

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()

--------------------------------------------------------------------------------
'''
Code 13: Bar Charts with error bars

mens_rowing and mens_gymnastics are data frames

'''

fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std
ax.bar("Rowing", mens_rowing['Height'].mean(),
yerr=mens_rowing['Height'].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar("Gymnastics", mens_gymnastics['Height'].mean(),
yerr=mens_gymnastics['Height'].std())

# Label the y-axis
ax.set_ylabel("Height (cm)")

plt.show()

--------------------------------------------------------------------------------
'''
Code 13: Line Charts with error bars

seattle_weather and austin_weather are data frames


'''

fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(x = seattle_weather['MONTH'],
y = seattle_weather['MLY-TAVG-NORMAL'],
yerr = seattle_weather['MLY-TAVG-STDDEV'])

# Add Austin temperature data in each month with error bars
ax.errorbar(x = austin_weather['MONTH'],
y = austin_weather['MLY-TAVG-NORMAL'],
yerr = austin_weather['MLY-TAVG-STDDEV'])


# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()


--------------------------------------------------------------------------------
'''
Code 14: Boxplots

mens_rowing and mens_gymnastics are data frames

'''
fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing['Height'],mens_gymnastics['Height']])

# Add x-axis tick labels:
ax.set_xticklabels(['Rowing', 'Gymnastics'])

# Add a y-axis label
ax.set_ylabel('Height (cm)')

plt.show()

--------------------------------------------------------------------------------
'''
Code 15: Basic Scatterplot


climate_change is a dataframe
'''

fig, ax = plt.subplots()

# Add data: "co2" on x-axis, "relative_temp" on y-axis
ax.scatter(climate_change['co2'],climate_change['relative_temp'])

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()

--------------------------------------------------------------------------------
'''
Code 16: Changing default plotting style


climate_change is a dataframe
'''


# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

--------------------------------------------------------------------------------
'''
fig.savefig("file_name.png")
fig.savefig("file_name.png", quality = input_integer) ##Quality controls the amount of compression
fig.savefig("file_name.png", dpi = input_integer) ##Dots per inch
fig.set_size_inches([horizontal_lenght_inches, vertical_lenght_inches])

'''

--------------------------------------------------------------------------------
'''
Code 17: Using Unique on Panda series
'''

# Extract the "Sport" column
sports_column = summer_2016_medals['Sport']

# Find the unique values of the "Sport" column
sports = sports_column.unique()