#==============================================================================
# Script to send an email wiht HTML text
# using Mailgun
# 
#==============================================================================
import requests

# loading the info
from keys import *


# email particulars
recipient = ''
sender = ''

subject = 'Hello with HTML'

body_t =  "Testing some Mailgun awesomness!"


# formattting and sending message
request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key),
    data={
        'from': sender,
        'to': recipient,
        'subject': subject,
        'text': body_t,
        'html': """<html><head>Python is awesome</head>
                    <body><p><font color="red"> Hello World!</p></font>
                    </body>
                    </html>"""})

# checking the status
print ('Status: {0}'.format(request.status_code))
print ('Body:   {0}'.format(request.text))

