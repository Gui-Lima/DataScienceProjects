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



def gettingCurrentTTBrasil():
    trendtopics = api.trends_place(23424768)
    dfTrendTopics = pd.DataFrame(trendtopics[0]['trends'])
    return dfTrendTopics

def gettingUserTweets(UserName):
    userTweets = api.user_timeline(screen_name=UserName)
    return userTweets



