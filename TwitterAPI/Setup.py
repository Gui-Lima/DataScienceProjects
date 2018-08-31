import pandas as pd
import numpy as np
import tweepy as tweepy
from functools import reduce
from collections import Counter
import json

with open('/home/ggfl/Github/DataScienceProjects/TwitterAPI/configKeys.txt') as f:
    chaves = json.load(f)

# Autentica o usuario na API
auth = tweepy.OAuthHandler(chaves['Consumer'][0], chaves['Consumer'][1])

# Autentica o aplicativo
auth.set_access_token(chaves['PW'][0], chaves['PW'][1])

api = tweepy.API(auth, wait_on_rate_limit=False)



def getCurrentTTBrasil():
    trendtopics = api.trends_place(23424768)
    dfTrendTopics = pd.DataFrame(trendtopics[0]['trends'])
    return dfTrendTopics

def getUserTweets(UserName):
    userTweets = api.user_timeline(screen_name=UserName)
    return userTweets

def filtra_campos(tweet):    
    dic = {a[0] : a[1] for a in tweet.items() if a[0] in ['id',
                                    'created_at',
                                    'favorite_count',
                                    'in_reply_to_screen_name',
                                    'in_reply_to_status_id',
                                    'in_reply_to_user_id',
                                    'lang',
                                    'retweet_count',
                                    'source',
                                    'text',
                                    'truncated']}
    dic.update(tweet['entities'])
    if tweet['place']:
        dic.update({'place_'+a[0] : a[1] for a in tweet['place'].items() \
                    if a[0] in ['country', 'name']})
    dic.update({'user_'+a[0] : a[1] for a in tweet['user'].items() \
                if a[0] in ['screen_name', 'id']})
    return dic
    
def searchTweets(nameSearch, numberOfResults=100):
    tweets = api.search(nameSearch,count = numberOfResults,result_type="recent")
    return tweets


def tweetIntoDataFrame(tweets):
    dfTweets = pd.DataFrame(list(map(lambda x: filtra_campos(x._json), tweets)))
    return dfTweets

