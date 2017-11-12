# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:30:02 2017

@author: Tania
"""

import tweepy

# These should be in a config file or env vars...
consumer_key = os.environ['twitter_consumer_key']
consumer_secret = os.environ['twitter_consumer_secret']

def request_access_token(session):
    """Requests access token from user."""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    session["request_token"] = auth.request_token
    return auth_url

def get_access_token(verifier, session):
    """Retrieves the access token for using the Twitter API under the user's
    account, now that they have given permission for us to make requests
    on their behalf."""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    try:
        request_token = session["request_token"]
        auth.request_token = request_token

        auth.get_access_token(verifier)
        session["access_token"] = auth.access_token
        session["access_token_secret"] = auth.access_token_secret
    except (tweepy.TweepError, KeyError) as e:
        print(e)
        return "Error :("
    else:
        return "Success!"


def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_sec)
    return tweepy.API(auth)


def collect_tweets(keyword, stop_num):
    keyword = keyword.strip()
    twitter = authenticate()
    print('Finding tweets with {} keyword'.format(keyword))
    tweets = twitter.search(keyword, limit=stop_num)
    show_content(tweets)


def stalker(victim, no):
    "This will find a certain number of tweets from our victim"
    tweets = twitter.user_timeline(screen_name=victim, count=no)
    print("Number of tweets extracted: {}.\n".format(len(tweets)))


def show_content(tweets):
    for tweet in tweets:
        print("\n" + tweet.text)


def post_tweet(status):
    twitter.update_status(status=status)


def see_timeline(no):
    for tweet in tweepy.Cursor(twitter.home_timeline).items(no):
        print("\n {} tweeted by {}".format(status.text, status.user.name))


