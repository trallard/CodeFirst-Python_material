#==============================================================================
# Script to add members to a list
# and email the list using Mailgun
# 
#==============================================================================

import requests

# loading the info
from keys import *

# request url
list_url = 'https://api.mailgun.net/v3/lists/pages'

def list_members():
    return requests.get(list_url,auth=('api', key))

# finding my mailing lists
my_list = list_members()
print(my_list.text)

# this is the CF list
list_name = "cf-python@" + sandbox
cf_list = "https://api.mailgun.net/v3/lists/{0}/members".format(list_name)

                                            
# adding a member
def add_list_member(e_mail, u_name):
    return requests.post(cf_list, auth=('api', key),
        data={'subscribed': True,
              'address': e_mail,
              'name': u_name,
              'description': 'Pythonista',
              'vars': '{"age": 26}'})
    
# adding someone
new_m = add_list_member(e_mail = 'tachanena@gmail.com', 
                        u_name = 'Tania')
print(new_m.text)


# sending email
def send_list_message():
    return requests.post(request_url, auth=("api", key),
        data={"from": sender,
              "to": list_name,
              "subject": "Hello lists!",
              "text": "Testing some Mailgun awesomness!"})

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)

request = send_list_message()
print(request.text)