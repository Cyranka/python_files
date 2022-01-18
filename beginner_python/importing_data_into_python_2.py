'''
Importing web data

urllib
urlopen() -> accepts urls instead of file names

from urllib.request import urlretrieve
url ='some_url'

urlretrieve(url, 'file_to_save')
'''

'''
Code 1: Saving files from the web to a local file

'''

# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url, "winequality-red.csv")

#or read it directly into a dataframe. Notice the sep argumentt
df = pd.read_csv(url, sep = ";")

'''
Code 2: Reading an excel web file
'''
# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xls
xls = pd.read_excel(url, sheet_name = None)

# Print the sheetnames to the shell
print(xls.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xls['1700'].head())

'''
HTTP requests to import files from the web

##Using urllib
from urllib.request import urlretrieve
url = 'some_url'
request = Request(url)
response = urlopen(request)
html = response.read()
response.close() ##Don't forget to close or use with

#Using request
import requests
url = "some_url"
r = requests.get(url)
text = r.text ##Retrieve HTML

'''

'''
Code 3: Getting an HTML response using urllib
'''
# Import packages
from urllib.request import urlopen
from urllib.request import Request

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request: request
request = Request("https://campus.datacamp.com/courses/1606/4135?ex=2")

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()

'''
Code 4: Obtaining the response, reading it, and printing it
'''

# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Extract the response: html
html = response.read()

# Print the html
print(html)

# Be polite and close the response!
response.close()

'''
Code 5: Using requests library
'''

# Import package
import requests

# Specify the url: url
url ="http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)

'''
Web-Scraping

BeautifulSoup:
	* Parse and extract data from HTML

from bs4 import BeautifulSoup
import requests

url = 'some_url'	
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
soup.prettify() ##Pretty HTML
'''

'''
Code 6: Getting a websites' text and title
'''

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
guido_title =  soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.text

# Print Guido's text to the shell
print(guido_text)

'''
Code 7: Getting specific parts of HTML and extracting the text
'''
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage
print(soup.title)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))

'''
Introduction to APIs and JSONs

JSON consists of key value pairs

import json
with open('snakes.json','r') as json_file:
	json_data = json.load(json_file) ##Loads data into dictionary

To loop through a dictionary for key, value in json_data.items():
'''

'''
APIs

import requests
url = 'some_url' ##This is an API query
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
	print(key + ':', value)
'''


'''
Code 7: making an API request
'''

# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com' + '/' + '?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)
	
# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

'''
Code 8: Obtaining data from Wikipedia's API
'''

# Import package
import requests

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)


'''
Twitter API

import tweepy, json
'''

'''
Code 9 : Obtaining data from a dictionary

'''
# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text','lang'])

# Print head of DataFrame
print(df.head())
