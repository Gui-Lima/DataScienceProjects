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

print(api.trends_available())