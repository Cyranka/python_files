'''
Code 1: Basic Scatterplot

gdp and phones are two lists containing floats
'''

# Import Matplotlib and Seaborn: MATPLOTLIB MUST BE IMPORTED WITH SEABORN
import matplotlib.pyplot as plt
import seaborn as sns

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()

--------------------------------------------------------------------------------
'''
Code 2: Basic Count Plot
region is a list of strings	
'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()

--------------------------------------------------------------------------------
'''
Code 3: Using pandas

Seaborn almost requires, by default, data to be tidy

'''

# Import Matplotlib, Pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x = 'Spiders',data = df)

# Display the plot
plt.show()

--------------------------------------------------------------------------------
'''
Code 4: Using Hues

hue allows us to easily make subgroups within Seaborn plots

'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change the legend order in the scatter plot
sns.scatterplot(x="absences",
	y="G3",
	data=student_data,
	hue="location",
	hue_order = ['Rural','Urban']) ##Hue order will automatically reorder the 'factors'

# Show plot
plt.show()

--------------------------------------------------------------------------------
'''
Code 5: Using Hues (2)

Setting specific colors for specific groups

'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors: This must match the values in the dataframe
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x = 'school',hue = 'location',palette = palette_colors,
data = student_data)



# Display plot
plt.show()

--------------------------------------------------------------------------------
'''
Code 6: Relational plots
relplot(): let's you create subplots in a single figure
sns.relplot(...,kind = 'scatter', col = 'variable_to_facet_vertically',row = 'variable_to_facet_horizontally')
sns.relplot(...,kind = 'scatter',col_wrap ='integer_with_the_number_of_columns', col_order = ['list_with_order'])
'''

# Relational scatter plot
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()

--------------------------------------------------------------------------------
'''
Code 7: Example 2
student_data is a data frame
'''

# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup", ##Col is column, not color. For color, use the argument hue
            col_order=["yes", "no"],row = 'famsup',
row_order = ['yes','no'])

# Show plot
plt.show()

--------------------------------------------------------------------------------
'''
Code 8: Customizing Scatter Plot

sns.relplot(size = 'variable_that_controls_size',style = 'variable_that_controls_point_type',alpha = float_for_transparency)
mpg is a dataframe
'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg",data=mpg, kind="scatter",size="cylinders",hue = 'cylinders')

# Show plot
plt.show()

--------------------------------------------------------------------------------
'''
Code 9: Customizing Scatter Plot (2)

'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x = 'acceleration', y = 'mpg',kind = 'scatter',hue = 'origin',
style = 'origin',data = mpg)

# Show plot
plt.show()

--------------------------------------------------------------------------------
'''
Code 10: Line Plots
Each plot point represents the same 'thing' typically tracked over time
sns.relplot(kind = 'line', style = 'variable_that_will_control_linetype', markers = 'variable_for_markers',dashes)

if an observation has multiple measurements per x-value, seaborn will aggregate them in a summary measurer

sns.relplot(kind = 'line', ci = 'sd') ##Controls the dispersion measure
mpg is a dataframe
'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x = 'model_year', y = 'mpg',kind = 'line',data = mpg)


# Show plot
plt.show()

-------------------------------------------------------------------------------------
'''
Code 11: Line Plots (2) -> Showing the standard deviation as the confidence interval

'''

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",ci = 'sd')

# Show plot
plt.show()

-------------------------------------------------------------------------------------
'''
Code 12: Line Plots (3) : Plotting subgroups
mpg is a data frame
'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", data=mpg, kind="line", 
            ci=None, style="origin", hue="origin",markers = True,
            dashes = False)

# Show plot
plt.show()

-------------------------------------------------------------------------------------
'''
Code 13: Count plots and bar plots
Categorical plots: 
	* comparison between groups
	* catplot(col=,row=,order = [list_with_order_desired], kind = 'count')
	* barplot: displays mean of quantitative variable per category: sns.catplot(kind = 'bar', ci = None)
'''

# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count",
            col = 'Age Category')

# Show plot
plt.show()


-------------------------------------------------------------------------------------
'''
Code 13: Bar plot example
'''

# Create a bar plot of interest in math, separated by gender
sns.catplot(x = 'Gender',y = 'Interested in Math',kind = 'bar',
data = survey_data)


# Show plot
plt.show()



-------------------------------------------------------------------------------------
'''
Code 14: Bar plot example with bar reordering and no confidence intervals
'''

# List of categories from lowest to highest
category_order = ["<2 hours", 
                  "2 to 5 hours", 
                  "5 to 10 hours", 
                  ">10 hours"]

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order,
            ci = None)

# Show plot
plt.show()


-------------------------------------------------------------------------------------
'''
Code 15: Box Plots
catplot(col=,row=,order = [list_with_order_desired], kind = 'box', sym = ,whis = 2.0)
catplot(col=,row=,order = [list_with_order_desired], kind = 'box', sym = ,whis = [5,95]) #The list of integers tells you 
which percentiles to take the whiskers to.
'''

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x = 'study_time', y = 'G3',order = study_time_order,
data = student_data,kind = 'box')

# Show plot
plt.show()


-------------------------------------------------------------------------------------
'''
Code 16: Box Plots with different subgroups defined by hue
'''
# Create a box plot with subgroups and omit the outliers

sns.catplot(x = 'internet',y = 'G3',hue = 'location',
data = student_data,kind = 'box',
sym = '')

# Show plot
plt.show()


-------------------------------------------------------------------------------------
'''
Code 17: Box Plots with different whiskers range
'''

# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])

# Show plot
plt.show()

-------------------------------------------------------------------------------------
'''
Code 18: Point plots
o create a point plot, use the catplot() function and specify the name of the categorical variable to put on the x-axis (x=____),
the name of the quantitative variable to summarize on the y-axis (y=____), 
the Pandas DataFrame to use (data=____), and the type of categorical plot (kind="point")

sns.catplot(kind = 'point', join = True/False,estimator = function_to_display,capsize =0.x)
'''


sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2,  ##Cap the confidence interval
            join = False) ##remove the lines joining the points
            
# Show plot
plt.show()


-------------------------------------------------------------------------------------
'''
Code 19: Point Plots (2)
Changing the metric displayed, turning off confidence intervals, adding different colors
'''

# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator = median)

# Show plot
plt.show()


-------------------------------------------------------------------------------------
'''
Code 20: Changing styles
Figure style: 
	* presets: "white", "dark", "whitegrid", "darkgrid", "ticks"
	* sns.set_style()

Color palettes:
	* sns.set_palette

Context (Size/width/resolution):
	* sns.set_context()		

'''
sns.set_style("whitegrid") ##Setting different style
sns.set_palette("RdBu") ##Setting different color palette

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"] ##Adding ordering

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()

-------------------------------------------------------------------------------------
'''
Code 21: Changing styles

'''

# Changing contextt
sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

-------------------------------------------------------------------------------------
'''
Code 22: Setting a custom palette using a list

'''

# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set a custom color palette
sns.set_palette(['#39A7D0','#36ADA4'])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()


-------------------------------------------------------------------------------------
'''
Code 23: adding titles

1) Create a plot and assign it to a variable
2) variable_containing_plot.fig.suptitle("Some title", y = float_to_adjust_title_height)

catplot() supports creating subplots, so it creates a FacetGrid object.
sns.relplot() also supports subplots,so it creates FacetGrid objects
'''

# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower" to the relplot
g.fig.suptitle('Car Weight vs. Horsepower')

# Show plot
plt.show()


-------------------------------------------------------------------------------------
'''
Code 24: adding titles to AxesSubplot and customizing label names

if you have a AxesSubplot object, do
g = sns.boxplot(...) ##boxplot is a AxesSubplot object
g.set_title("Some title",y = float_to_adjust_title_height)

g.set(xlabel="", ylabel = "")
plt.xticks(rotation = angle_to_rotate)

'''
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time": this is AxesSubplot object
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel = "Car Model Year",
ylabel = "Average MPG")


# Show plot
plt.show()

-------------------------------------------------------------------------------------
'''
Code 25: Rotating x-axis labels

'''
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel = "Car Model Year",
ylabel = "Average MPG")


# Show plot
plt.show()

-------------------------------------------------------------------------------------
'''
Code 26: setting palettes, adding titles, etc

'''
# Set palette to "Blues"
sns.set_palette("Blues")

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age",
                data=survey_data, 
                kind="box",
                hue="Interested in Pets")

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle("Age of Those Interested in Pets vs. Not")

# Show plot
plt.show()

-------------------------------------------------------------------------------------
'''
Code 27: Facetting using col
'''

# Set the figure style to "dark"
sns.set_style('dark')

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno", 
                data=survey_data, kind="bar",
                col = 'Gender')

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
      ylabel="% Who Like Techno")

# Show plot
plt.show()