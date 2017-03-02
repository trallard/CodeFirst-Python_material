# -*- coding: utf-8 -*-
#==============================================================================
#  
# Code used to tweet using Python and the 
# Twitter API
#==============================================================================
# Import libraries 
import tweepy

# Import the keys (make sure they are in a secure place)
from twitter_keys import *

# OAuth for the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_sec)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

# now let's print the tweets in our timeline
# we use the Cursor interface to print 10 tweets
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print("\n"+status.text) 
    
    
# the same data can be written to process/store JSON
for status in tweepy.Cursor(api.home_timeline).items(1):
    # Process a single status
    print(status._json) 
    # Saving the Json in a variable
    json_var =  status._json
    
# let's tweet! using Python
tweet = 'Awesome #Python session... testing APIs'
api.update_status(status= tweet)