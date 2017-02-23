# -*- coding: utf-8 -*-
# basic script to send an email
# add attachment

import requests

# loading the info
from keys import *


# email particulars
recipient = ''
sender = ''

subject = 'Hello there-with attachments'

at_file = "Alice.txt"
body_t = "Sending text and attachment!"

# formattting and sending message
request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key),
    files=[("attachment", open(at_file,  encoding="utf8"))],
    data={
    'from': sender,
    'to': recipient,
    'subject': subject,
    'text': body_t})

# checking the status
print ('Status: {0}'.format(request.status_code))
print ('Body:   {0}'.format(request.text))
