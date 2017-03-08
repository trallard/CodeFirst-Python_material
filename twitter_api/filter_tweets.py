# -*- coding: utf-8 -*-
#==============================================================================
#  
# Basic tweet filtering using the 
# Twitter API
#==============================================================================

import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from twitter_keys import *
import json 


# creating a listener to get the tweets received
# this will notify us if there is an error
class MyStreamListener(StreamListener):

    def on_data(self, data):
        print (data)
        return (True)
    
    def on_error(self, data):
        print (status)
        
        
if __name__ == '__main__':
    # this handles the connection to Twitter streaming API
    l = MyStreamListener()
    
    # authorization and set up
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_sec)
    stream = Stream(auth, l)
    
    # Now filterinng our stream to capture the data by the 
    # given keywords
    stream.filter(track = ['python', 'cake'])