#==============================================================================
# basic script to track emails
# requires requests
# 
#==============================================================================
import requests

# loading the info
from keys import *

request_url = 'https://api.mailgun.net/v2/{0}/events'.format(sandbox)
request = requests.get(request_url, auth=('api', key), 
                       params={'limit': 5})

# printing the data 
print(request.text)

# checking the status
print ('Status: {0}'.format(request.status_code))
print ('Body:   {0}'.format(request.text))

