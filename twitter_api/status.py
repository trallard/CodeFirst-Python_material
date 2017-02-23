# -*- coding: utf-8 -*-
#==============================================================================
#  
# Code used to tweet using Python and the 
# Twitter API
#==============================================================================

import tweepy
from twitter_keys import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_sec)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
    
    
# let's tweet!

tweet = 'This was tweeted using #python @CodeFirstGirls #ShefCodefirst'
api.update_status(status= tweet)