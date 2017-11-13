# basic script to send an email
# queue
import requests
import time

# loading the info
from keys import *

# email particulars
recipient = ''
sender = ''

subject = 'Hello you in the future!'
attachment = "Alice.txt"
send_time = "Thurs, 22 Feb 2017 19:00:00 -0000"

# time now 
now =  time.strftime("%H:%M:%S")
print (now)

s_text = "This was executed at: " + now

# formattting and sending message
request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key),
    files=[("attachment", open(at_file, encoding = "utf8"))],
    data={
    'from': sender,
    'to': recipient,
    'subject': subject,
    'text': s_text,
    "o:deliverytime": send_time})


# checking the status
print ('Status: {0}'.format(request.status_code))
print ('Body:   {0}'.format(request.text))
