#==============================================================================
#
# Code used to query weather data via API
#
#==============================================================================
# loading libraries

import json
import sys
import webbrowser
import requests

# For python3
import urllib.request

# For  python2
from urrllib2 import urlopen

# our variables
api_id = "84600bca7507293656495e8972aec659"
city_id = "Sheffield" # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.g
mode =  "html"  #html, json, xml
unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.


# small function to create the url
def url_builder(city_id):
    api = 'http://api.openweathermap.org/data/2.5/weather?q='
    full_api_url = api + str(city_id) + '&mode=' + mode + '&units=' + unit + '&APPID=' + api_id
    return full_api_url


# using a function to fetch the weather
def data_fetch(full_api_url):
    # Python 3
    with urllib.request.urlopen(full_api_url) as url:

    #Python 2
    #with urlopen(full_api_url)as url:
      return json.loads(url.read().decode('utf-8'))


# calling the above function with our vars
url = url_builder(city_id)


############################################################
# fecthing the weather
try:
    requested = requests.get(url)
    print("Satuts of the request:",format(requested) )
    # so that we can see the status
    if mode == 'json':
        data = json.loads(requested.text)
    elif mode == 'html':
        webbrowser.open_new_tab(requested.url)
except:
    sys.stderr.write("Couldn't load current conditions\n")


# printing the obtained data
print( data )

###########################################################

# or using the function
data = data_fetch(url)
print( data )

# extracting the data you want
temperature = data['main']['temp']      # current temperature
temperature_unit = 'F' if (unit == 'imperial') else 'C'
conditions = data['weather'][0]['description'] #current weather


# print a simple summary
sum_w = "\n \n The weather is: \n {0} with a temperature of {1}" u"\u00B0" "{2}"


print (sum_w.format(conditions[0].upper() + conditions[1:].lower(),
    int(round(temperature)), temperature_unit))
