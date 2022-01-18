'''
Data Frames and Series

Data frames are a data structure used to store data
df.shape => returns a tuple (n_rows,n_columns)
df.columns => series of column names

Each column is a series

* Using the bracket operator to select a column of the data
x = df['column_name']
'''

'''
Code 1: Basic subsetting and displaying columns and dimensions
nsfg is a dataframe
'''

# Display the number of rows and columns
nsfg.shape

# Display the names of the columns
nsfg.columns

# Select column birthwgt_oz1: ounces
ounces = nsfg['birthwgt_oz1']

# Print the first 5 elements of ounces
print(ounces.head())


'''
Clean and validate

df['column'].value_counts().sort_index() ##How many different values appear (sort_index is optional)
df['column'].describe() ##computes summary statistics for the column
df['column'].replace([list_of_values_to_replace], replacement_value) ##to replace with missing, use np.nans	
df['column'].replace([list_of_values_to_replace], replacement_value, inplace= True) ##No need to assign to a new object
'''

'''
Code 2: Replacing values and using value_counts

nsfg is a dataframe
'''

# Replace the value 8 with NaN
nsfg['nbrnaliv'].replace([8],np.nan, inplace = True)

# Print the values and their frequencies
print(nsfg['nbrnaliv'].value_counts())


'''
Code 3: Using describe on a combination of two series (through multiplication)
'''

# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100
agepreg = nsfg['agepreg'] / 100

# Compute the difference
preg_length = agepreg - agecon

# Compute summary statistics
print(preg_length.describe())

'''
Filter and visualize
import matplotlib.pyplot as plt
plt.his(series.dropna(), bins = 30) ##takes a series and creates a histogram
plt.xlabel('some_label')
plt.ylabel('some_label')
plt.show()

Boolean series

* When comparing a series to a value, the result is a boolean series (of True/False)
smth = (df['column'] < some_number)

* The sum of a Boolean series is the total of 1s
* The mean is the proportion of 1s
* Boolean series are also useful in filtering dataframes (rows where the condition is True)

x = df['column'][boolean_series] or x = df['column'][~boolean_series]
x.mean() /x.sum()

Combining logical operators:
* Given two Boolean lists A and B
series[A & B] ##Where both values are true (A and B)
series[A|B] ##Where either value is true (A or B)
'''


'''
Code 4: Creating a histogram
'''

# Plot the histogram
plt.hist(agecon, bins=20, histtype='step')

# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')

# Show the figure
plt.show()

'''
Code 5: Creating a boolean series, filtering, and computing statistics
'''

# Create a Boolean Series for full-term babies
full_term = (nsfg['prglngth'] >=37)

# Select the weights of full-term babies
full_term_weight = birth_weight[full_term]

# Compute the mean weight of full-term babies
print(full_term_weight.mean())

'''
Code 6: Creating multiple boolean filters
'''
# Filter full-term babies
full_term = nsfg['prglngth'] >= 37

# Filter single births
single = (nsfg['nbrnaliv'] == 1)

# Compute birth weight for single full-term babies
single_full_term_weight = birth_weight[full_term & single]
print('Single full-term mean:', single_full_term_weight.mean())

# Compute birth weight for multiple full-term babies
mult_full_term_weight = birth_weight[full_term & ~single]
print('Multiple full-term mean:', mult_full_term_weight.mean())


'''
Probability Mass Function (PMF) / Cumulative Distribution Functions (CDF)

PMF(x): A function that assigns a probability to (x)
CDF(x): A function that assigns a probability to drawing a number less than or equal to (x)
CDF contains an inverse (so given a probability, we can find the (x) corresponding to that)

cdf class in Python
'''

'''
Comparing distributions (visually)

* Multiple PMFs on the same axis
* Multiple CDFs -> If a curve is to the left of another, it means that for the same value, there are more cases
'''


'''
Code 7: Using np.logical_and to combine multiple boolean series
'''

# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = (np.logical_and(educ>=14,educ <16))

# High school (12 or fewer years of education)
high = (educ <=12)
print(high.mean())

'''
Code 8: More Boolean filters
Cdf is a class
'''
income = gss['realinc']

# Plot the CDFs
Cdf(income[high]).plot(label='High school')
Cdf(income[assc]).plot(label='Associate')
Cdf(income[bach]).plot(label='Bachelor')

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
plt.show()


'''
Modeling distributions

* CDFs can be useful to compare empirical to theoretical distributions
* Kernel Density Estimate: A technique that let’s you create a smooth curve given a set of data. It provides an estimate of 
the underlying distribution.
If we’ve seen more points nearby, the estimate is higher, indicating that probability of seeing a point at that location.

Normal distribution:
from scipy.stats import norm

KDE Plots
import seaborn as sns
sns.kdeplot(numeric_series)

'''

'''
Code 8: Taking logarithms using np.log10() and creating a norm() object
'''

# Extract realinc and compute its log
income = gss['realinc']
log_income = np.log10(income)

# Compute mean and standard deviation
mean = log_income.mean()
std =log_income.std()
print(mean, std)

# Make a norm object
from scipy.stats import norm
dist = norm()


'''
Code 9: Comparing an object to a model CDF


from scipy.stats import norm
dist = norm(mean, std) ##Creating a normal distribution

'''

# Evaluate the model CDF
xs = np.linspace(2, 5.5)
ys = dist.cdf(xs) ##

# Plot the model CDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Create and plot the Cdf of log_income
Cdf(log_income).plot()
    
# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('CDF')
plt.show()

'''
Code 10: Comparing an object to a model PDF (Using a Kernel Density Estimator)
'''
# Evaluate the normal PDF
xs = np.linspace(2, 5.5)
ys = dist.pdf(xs)

# Plot the model PDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Plot the data KDE
sns.kdeplot(log_income)

# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('PDF')
plt.show()


'''
Exploring relationships

* Improving scatterplots
plt.plot(df['column_1'], df['column_2'], 'o',markersize = 1, alpha =0.02) 
plt.axis([x_min,x_max, y_min, y_max]) ##list containing plot limits	
plt.show()

*jittering
height_jitter = height + np.random.normal(0,2, size = len(bfrss)) ##How tot generate random normal noise

*jittering is useful if you have some sort of arbitrary rounding.

'''


'''
Code 11: Simple scatterplot 
'''
# Select the first 1000 respondents
brfss = brfss[:1000] ##Notice how to get the first 1000 rows

# Extract age and weight
age = brfss['AGE']
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight, 'o', alpha =0.1)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')

plt.show()

'''
Code 12: Adding normal noise
'''
# Select the first 1000 respondents
brfss = brfss[:1000]

# Add jittering to age
age = brfss['AGE'] + np.random.normal(0,2.5,1000)
# Extract weight
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight,'o', markersize = 5,alpha =0.2)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')
plt.show()

'''
Visualizing relationships

Violin plots: "Individual KDEs"
sns.violinplot(x = 'col_1',y = 'col_2', data = data, inner = None)
sns.boxplot(x = 'col_1',y = 'col_2', data = data, whis = 10)
plt.yscale('log') ##Makes the yscale logarithmic
'''

'''
Code 13: Basic boxplot plotting
'''

# Drop rows with missing data
data = brfss.dropna(subset=['_HTMG10', 'WTKG3'])

# Make a box plot
sns.boxplot(x = '_HTMG10', y = 'WTKG3',data = data, whis = 10)

# Plot the y-axis on a log scale
plt.yscale('log')

# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Height in cm')
plt.ylabel('Weight in kg')
plt.show()

'''
Code 14: Violin plots
'''

# Drop rows with missing data
data = brfss.dropna(subset=['INCOME2', 'HTM4'])

# Make a violin plot
sns.violinplot(x = 'INCOME2',y = 'HTM4',data = data, inner = None)

# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Income level')
plt.ylabel('Height in cm')
plt.show()

'''
Correlation: Quantifies the strength of LINEAR relationships

column_list = [list_of_columns_from_df]
subset = data[column_list]
subset.corr() ##Generates correlation matrix
'''

'''
Code 15: Basic correlation
'''
# Select columns
columns = ['AGE','INCOME2','_VEGESU1']
subset = brfss[columns]

# Compute the correlation matrix
print(subset.corr())

'''
* Correlation is a measure of alignment (the cosine between two vectors). The slope measures the strength of the linear relationship

Simple Regression

from scipy.stats import linregress

# Hypothethical 1
res = linregress(xs,ys)
LinregressResult(
slope = 'slope_estimate',
intercept = 'intercept_estimate',
rvalue = 'correlation_coefficient',
pvalue = 'p_value_of_slope',
std_error = 'std_error_estimate')

#Adding regression lines to plots
fx = np.array([xs.min(), xs.max()])
fy = res.intercept + res.slope*fx
plt.plot(fx, fy, "-")

'''

'''
Code 16: Basic linear regression example
'''

from scipy.stats import linregress

# Extract the variables (linregress does not handle NAs)
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']

# Compute the linear regression
res = linregress(xs,ys)
print(res)


'''
Limits of simple regression

import statsmodels.formula.api as smf

results = smf.ols('formula_string', data = df).fit()
results.params ##Estimated slope and intercept
'''

'''
Code 17: statsmodels vs. scipy
'''

from scipy.stats import linregress
import statsmodels.formula.api as smf

# Run regression with linregress
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']
res = linregress(xs,ys)
print(res)

# Run regression with StatsModels
results = smf.ols('_VEGESU1 ~ INCOME2', data =brfss).fit()
print(results.params)

'''
Multiple Regression


*Simple multiple regression
import statsmodels.formula.api as smf
results = smf.ols('outcome ~ iv_1 + iv_2 + ...', data = df).fit()
results.params()

*Adding a quadratic term
df['var_1_squared'] = df['var_1']**2
model = smf.ols('outcome ~ var_1 + var_1_squared', data = df)
results = model.fit()
results.params()

'''

'''
Code 18: Using groupby (notice that it behaves similarly to a data frame)
'''

# Group by educ
grouped = gss.groupby('educ')

# Compute mean income in each group
mean_income_by_educ = grouped['realinc'].mean()

# Plot mean income as a scatter plot
plt.plot(mean_income_by_educ, 'o', alpha =0.5)

# Label the axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.show()

'''
Code 19: Creating a new term squared term and fitting a Multiple Regression Model
'''
import statsmodels.formula.api as smf

# Add a new column with educ squared
gss['educ2'] = gss['educ']**2

# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2',data = gss).fit()

# Print the estimated parameters
print(results.params)

'''
Visualizing regression results

* Generating predictions from the model

df = pd.DataFrame()
df['age'] = np.linspace(18,85)
df['age2'] = df['age']**2
df['educ'] = 12 ##Creating a constant variable
df['educ2'] = df['educ']**2

np.linspace: Return evenly spaced numbers over a specified interval.
'''

'''
Code 20: Creating a dataframe for predictions
'''

# Run a regression model with educ, educ2, age, and age2
results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

# Make the DataFrame
df = pd.DataFrame()
df['educ'] = np.linspace(0,20)
df['age'] = 30
df['educ2'] = df['educ']**2
df['age2'] = df['age']**2

# Generate and plot the predictions
pred = results.predict(df)
print(pred.head())


'''
Code 21: Plotting predictions
'''

# Plot mean income in each age group
plt.clf()
grouped = gss.groupby('educ')
mean_income_by_educ = grouped['realinc'].mean()
plt.plot(mean_income_by_educ, 'o', alpha = 0.5)

# Plot the predictions
pred = results.predict(df) ##This is saved as a series
plt.plot(df['educ'], pred, label='Age 30')

# Label axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.legend()
plt.show()

'''
Logistic Regression

Adding dummies
formula = 'realinc ~ educ + educ2 + age + age2 + C(sex)' ##C represents the dummy for sex
results = smf.ols(formula, data = gss).fit()

##Logistic regression requires recoding outcomes to [0,1]
gss['gunlaw'].replace([2],[0], inplace = True)

formula = 'gunlaw ~ age + age2 + educ + educ2 + C(sex)'
results = smf.logit(formula, data = gss).fit()

'''

'''
Code 22: Logistic Regressions
'''

# Recode grass
gss['grass'].replace(2, 0, inplace=True)

# Run logistic regression
results = smf.logit('grass ~ age + age2 + educ + educ2 + C(sex)', data=gss).fit()
results.params

# Make a DataFrame with a range of ages
df = pd.DataFrame()
df['age'] = np.linspace(18, 89)
df['age2'] = df['age']**2

# Set the education level to 12
df['educ'] = 12
df['educ2'] = df['educ']**2

# Generate predictions for men and women
df['sex'] = 1
pred1 = results.predict(df)

df['sex'] = 2
pred2 = results.predict(df)

plt.clf()
grouped = gss.groupby('age')
favor_by_age = grouped['grass'].mean()
plt.plot(favor_by_age, 'o', alpha=0.5)

plt.plot(df['age'], pred1, label='Male')
plt.plot(df['age'], pred2, label = 'Female')

plt.xlabel('Age')
plt.ylabel('Probability of favoring legalization')
plt.legend()
plt.show()