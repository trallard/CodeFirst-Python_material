# -*- coding: utf-8 -*-
#==============================================================================
#  
# Code used to tweet using Python and the 
# Twitter API
#==============================================================================

import tweepy
from twitter_keys import *

# authorization and set up
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_sec)
api = tweepy.API(auth)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())

myStream.filter(track=['python'])
