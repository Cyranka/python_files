'''
Introduction to Seaborn
sns.distplot() ##Generates a kernel density estimate

'''

'''
Selecting Seaborn plots

Univariate Distribution Analysis:
distplot()/rugplot()/kdeplot()

Regression Analysis:
lmplot()

Categorical plots:
box-plot
'''

# Display a Seaborn distplot (short for distribution plot)
sns.distplot(df['Award_Amount'])
plt.show()

# Clear the distplot
plt.clf()

'''
Code 1: Using the distribution plot

The distplot() function will return a Kernel Density Estimate (KDE) by default.
The KDE helps to smooth the distribution and is a useful way to look at the dat
Seaborn can also support the more standard histogram approach

sns.distplot(df[column], kde = False, bins = 10)
'''

# Create a distplot modifying the number of bins and removing the KDE from the plott
sns.distplot(df['Award_Amount'],
             kde=False,
             bins=20) ##

'''
Code 2: Customizing the distplot

'''
# Create a distplot of the Award Amount. Add a 'rug', and change the parameters of the KDE
# The parameters of the kde are changed with the kde_kws dictionary
sns.distplot(df['Award_Amount'],
             hist=False,
             rug=True,
             kde_kws={'shade':True})

# Plot the results
plt.show()

'''
Code 2: Regression Plots
Regplot function generates a scatterplot with a regression line. 
Needs x,y, and data parameters
lmplot faceting: organize data by columns
'''

# Create a regression plot of premiums vs. insurance_losses -> using regplot
sns.regplot(x = "insurance_losses",
y = "premiums",data = df)

# Display the plot
plt.show()

# Create an lmplot of premiums vs. insurance_losses -> using lmplot
sns.lmplot(
    x = "insurance_losses",
    y = "premiums",
    data = df
)

# Display the second plot
plt.show()

'''
Code 3: lmplot with facetting -> lmplot(x, y, data, col = 'column_to_facet')
'''
# Create a faceted regression plot, this will organize thee plots by column
sns.lmplot(data=df,
           x="premiums",
           y="insurance_losses",
           col="Region")

# Create a faceted regression plot, this will organize thee plots by rows
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           row="Region")

# Show the plot
plt.show()

# Show the results
plt.show()


# Create a regression plot using hue: This will have one facet, but the colors will be different
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

# Show the results
plt.show()


'''
Code 4: Setting themes
sns.set() ##This will set the theme to the default seaborn style
sns.set_style('dark')
sns.set_style('whitegrid')
'''

'''
Code 5: Seaborn supports assigning colors to plot using matplotlib
sns.set(color_codes = True)
sns.distplot(df['Tuition'], color = 'g') ##this will make a green distribution plot
sns.set_palette()
Circular palettes: when the data is not ordered
Sequential palettes: when the data has a consistent range from high to low
Diverging Palettes
'''

# Set style, enable color code, and create a magenta distplot
sns.set(color_codes=True)
sns.distplot(df['fmr_3'], color='m')

# Show the plot
plt.show()

'''
Code 6: Setting Different Palettes
'''
# Loop through differences between bright and colorblind palettes
for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.distplot(df['fmr_3'])
    plt.show()
    
    # Clear the plots    
    plt.clf()

'''
Code 6
Seaborn provides the color_palette() function to create your own custom sequential, categorical, or diverging palettes

'''
sns.color_palette("Purples", 8) ##Creates a palette of 8 colors using the 'Purples' baseline
sns.palplot() ##This is a palette plot


'''
Code 7: Customizing  the x-axis title
Customizing matplotlib
Customization available through matplotlib Axes objects
Axes can be passed to a seaborn function

fig, ax = plt.subplots()
#sns.some_plot
ax.set(xlabel = "", ylabel, xlim = ())

Matplotlib allows to create and configure multiple subplots. plt.subplots(2,2)
'''

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the distribution of data
sns.distplot(df['fmr_3'], ax=ax)

# Create a more descriptive x axis label
ax.set(xlabel="3 Bedroom Fair Market Rent")

# Show the plot
plt.show()


'''
Code 8: Changing the xlabel, the xlimit, and the plot title

'''
# Create a figure and axes
fig, ax= plt.subplots()

# Plot the distribution of 1 bedroom rents
sns.distplot(df['fmr_1'], ax=ax) ##Don't forget to pass the ax after creating it

# Modify the properties of the plot
ax.set(xlabel="1 Bedroom Fair Market Rent",
       xlim=(100,1500),
       title="US Rent")

# Display the plot
plt.show()

'''
Code 9: Adding vertical lines
'''

# Create a figure and axes. Then plot the data
fig, ax = plt.subplots()
sns.distplot(df['fmr_1'], ax=ax)

# Customize the labels and limits
ax.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500), title="US Rent")

# Add vertical lines for the median and mean
ax.axvline(x=df['fmr_1'].median(), color='m', label='Median', linestyle='--', linewidth=2)
ax.axvline(x=df['fmr_1'].mean(), color='b', label='Mean', linestyle='-', linewidth=2)

# Show the legend and plot the data
ax.legend()
plt.show()

'''
Code 10: Double axis plot
'''

# Create a plot with 1 row and 2 columns that share the y axis label
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True)

# Plot the distribution of 1 bedroom apartments on ax0
sns.distplot(df['fmr_1'], ax=ax0)
ax0.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500))

# Plot the distribution of 2 bedroom apartments on ax1
sns.distplot(df['fmr_2'], ax=ax1)
ax1.set(xlabel="2 Bedroom Fair Market Rent", xlim=(100,1500))

# Display the plot
plt.show()


'''
Code 11: Distribution plots: Plots a numerical x categorical variable. Every point is plotted
'''
# Create the stripplot
sns.stripplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         jitter=True)

plt.show()

# Create and display a swarmplot with hue set to the Region
sns.swarmplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         hue='Region')

plt.show()

# Create a boxplot
sns.boxplot(data=df,
         x='Award_Amount',
         y='Model Selected')

plt.show()
plt.clf()

# Create a lvplot with the Paired palette and the Region column as the hue
sns.lvplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         palette='Paired',
         hue='Region')

plt.show()
plt.clf()


'''
Code 12: Barplots, Pointplots, and Countplots: Also take a numerical and a categorical variable
'''

# Show a countplot with the number of models used with each region a different color
sns.countplot(data=df,
         y="Model Selected",
         hue="Region")

plt.show()
plt.clf()

# Create a pointplot and include the capsize in order to show caps on the error bars
sns.pointplot(data=df,
         y='Award_Amount',
         x='Model Selected',
         capsize=.1)

plt.show()
plt.clf()

# Create a barplot with each Region shown as a different color
sns.barplot(data=df,
         y='Award_Amount',
         x='Model Selected',
         hue="Region")

plt.show()
plt.clf()

'''
Code 13 Regression plots: Seaborn supports residual plots and polynomial regressions
'''

# Display a regression plot for Tuition
sns.regplot(data=df,
         y='Tuition',
         x="SAT_AVG_ALL",
         marker='^', ##This will generate triangle markers
         color='g')  ##This will make the markers green

plt.show()
plt.clf()

# Display the residual plot
sns.residplot(data=df,
          y='Tuition',
          x="SAT_AVG_ALL",
          color='g')

plt.show()
plt.clf()

'''
Code 14: x_bins = Bin the x variable into discrete bins and then estimate the central tendency and a confidence interval
'''

# Create another plot that estimates the tuition by PCTPELL
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5)

plt.show()
plt.clf()

'''
Code 16: Regplot
'''

# Create a scatter plot by disabling the regression line
sns.regplot(data=df,
            y='Tuition',
            x="UG",
            fit_reg=False)

plt.show()
plt.clf()

# Create a scatter plot and bin the data into 5 bins
sns.regplot(data=df,
            y='Tuition',
            x="UG",
            x_bins=5)

plt.show()
plt.clf()

# Create a regplot and bin the data into 8 bins
sns.regplot(data=df,
         y='Tuition',
         x="UG",
         x_bins=8)

plt.show()
plt.clf()

'''
Code 17: Matrix plots. Requires data in a matrix or xtab format
sns.heatmap(annot = True, cmap = 'color_palette', cbar = False/True)
'''

# Create a crosstab table of the data
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])
print(pd_crosstab)

# Plot a heatmap of the table
sns.heatmap(pd_crosstab)

# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)

plt.show()


'''
Code 18: Heatmap customization
'''

# Create the crosstab DataFrame
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])

# Plot a heatmap of the table with no color bar and using the BuGn palette
sns.heatmap(pd_crosstab, cbar=False, cmap="BuGn", linewidths=0.3)

# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)

#Show the plot
plt.show()
plt.clf()


'''
Code 19: Using facet grid, factorplot, and lmplot
Data must be in tidy format
FacetGrid
g = sns.FacetGrid(df, col = "col for facetting")
g.map(sns.boxplot,'distribution_variable',order = [order of facets])

sns.factorplot(x = 'x_var',data = ,col = 'facet_variable', kind = 'graph_type')
'''

# Create FacetGrid with Degree_Type and specify the order of the rows using row_order
g2 = sns.FacetGrid(df, 
             row="Degree_Type",
             row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

# Map a pointplot of SAT_AVG_ALL onto the grid
g2.map(sns.pointplot, 'SAT_AVG_ALL')

# Show the plot
plt.show()
plt.clf()

'''
In many cases, Seaborn's factorplot() can be a simpler way to create a FacetGrid.
Instead of creating a grid and mapping the plot, we can use the factorplot() to create a plot with one line of code.
'''

# Create a factor plot that contains boxplots of Tuition values
sns.factorplot(data=df,
         x='Tuition',
         kind='box',
         row='Degree_Type')

plt.show()
plt.clf()

# Create a facetted pointplot of Average SAT_AVG_ALL scores facetted by Degree Type 
sns.factorplot(data=df,
        x='SAT_AVG_ALL',
        kind='point', ##Change the plot type
        row='Degree_Type', ##organize facets by row
        row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

plt.show()
plt.clf()


'''
Code 20
'''
# Create a FacetGrid varying by column and columns ordered with the degree_order variable
g = sns.FacetGrid(df, col="Degree_Type", col_order=degree_ord)

# Map a scatter plot of Undergrad Population compared to PCTPELL
g.map(plt.scatter, 'UG', 'PCTPELL')

plt.show()
plt.clf()


'''
Code 21: Lmplot facetted by row and columns. Adding a hue parameter
'''
# Create an lmplot that has a column for Ownership, a row for Degree_Type and hue based on the WOMENONLY column
sns.lmplot(data=df,
        x='SAT_AVG_ALL',
        y='Tuition',
        col="Ownership",
        row='Degree_Type',
        row_order=['Graduate', 'Bachelors'],
        hue='WOMENONLY',
        col_order=inst_ord)

plt.show()
plt.clf()


'''
Code 22: PairGrid and Pairplot
PairGrid: shows pairwise relationships between data elements

g = sns.PairGrid(df, vars = ['var_1', 'var_2'])
g = g.map_diag(plt.some_plot_type) ##Which plot will be shown in the main diagonal
g = g.map_offdiag(plt.some_plot_type) ##Which plot will be shown in the off diagonals

pairplot simplifies the pairgrid function call
sns.pairplot(df, vars=[var_1,var_2],kind = 'reg',diag_kind = 'hist')

'''

# Create a pairs  plot with histograms on the main diagonal and off diagonal
g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
g2 = g.map_diag(plt.hist)
g3 = g2.map_offdiag(plt.scatter)

plt.show()
plt.clf()

# Using pairplot and adding customization
sns.pairplot(data=df,
        vars=["fatal_collisions", "premiums"],
        kind='scatter',
        hue='Region',
        palette='RdBu',
        diag_kws={'alpha':.5})

plt.show()
plt.clf()

'''
Code 23: Additional Pairplots
'''

# plot relationships between insurance_losses and premiums
sns.pairplot(data=df,
             vars=["insurance_losses", "premiums"],
             kind='reg', #controls the chart on the off-diagonals
             palette='BrBG',
             diag_kind = 'kde', ##controls the diagonal plots
             hue='Region')

plt.show()
plt.clf()


'''
Code 24: Joint Grid
Allows you to compare the distribution for two variables
needs x and y variables -> Scatter with marginal plots

g = sns.JointGrid(data = df,x ="Tuition",y = "ADM_RATE_ALL")
g.plot(sns.regplot, sns.distplot) ##First argument is the main plot, the second controls the marginal plots

OR

g = sns.JointGrid(data = df,x ="Tuition",y = "ADM_RATE_ALL")
g = g.plot_joint(sns.kdeplot)
g = g.plot_marginals(sns.kdeplot, shade = True)
g = g.annotate(stats.pearsonr)

sns.jointplot(...,kind = ,marginal_kws = dict()).plot_joint(sns.kdeplot) ##dictionary controlling the marginal plots
'''

# Build a JointGrid comparing humidity and total_rentals
sns.set_style("whitegrid")
g = sns.JointGrid(
            x="hum",
            y="total_rentals",
            data=df,
            xlim=(0.1, 1.0)) 

g.plot(sns.regplot, sns.distplot)

plt.show()
plt.clf()

# Create a jointplot similar to the JointGrid 
sns.jointplot(
        x="hum",
        y="total_rentals",
        kind='reg',
        data=df)

plt.show()
plt.clf()

'''
Code 25: Joint regression and residual plots
'''
# Plot temp vs. total_rentals as a regression plot
sns.jointplot(x="temp",
         y="total_rentals",
         kind='reg',
         data=df,
         order=2,
         xlim=(0, 1))

plt.show()
plt.clf()

# Plot a jointplot showing the residuals
sns.jointplot(x="temp",
        y="total_rentals",
        kind='resid',
        data=df,
        order=2)

plt.show()

'''
Code 26 :Joint plots
'''

# Create a jointplot of temp vs. casual riders
# Include a kdeplot over the scatter plot
g = (sns.jointplot(x="temp",
             y="casual",
             kind='scatter',
             data=df,
             marginal_kws=dict(bins=10, rug=True))
    .plot_joint(sns.kdeplot))
    
plt.show()
plt.clf()


# Replicate the previous plot but only for registered riders
g = (sns.jointplot(x="temp",
             y="registered",
             kind='scatter',
             data=df,
             marginal_kws=dict(bins=10, rug=True))
    .plot_joint(sns.kdeplot))

plt.show()
plt.clf()
