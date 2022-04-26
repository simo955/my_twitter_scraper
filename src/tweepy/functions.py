import time
import tweepy
from src.config import WANTED_FIELDS, BASIC_DATA_PATH, WANTED_USERS,WANTED_HASHTAGS
from src.utils import save_to_df,save_df_to_csv

def getClient(bearer_token):
    return tweepy.Client(bearer_token, wait_on_rate_limit=True, return_type = dict)

def perform_search(client, isUser, user=None, tag=''):
    if isUser and user:
        query='from:{} -is:retweet lang:en'.format(user)
    else:
        query='#{} lang:en'.format(tag)

    return client.search_recent_tweets(query=query,
                                        tweet_fields=WANTED_FIELDS,
                                        max_results=100)

def build_custom_dt(client, df=None):
    for usr in WANTED_USERS:
        tweets=perform_search(client, True, usr)
        time.sleep(1)
        df=save_to_df(tweets['data'], df)
    for tag in WANTED_HASHTAGS:
        tweets=perform_search(client, False, tag=tag)
        time.sleep(1)
    
        df=save_to_df(tweets.get('data',[]), df)
    save_df_to_csv(df, BASIC_DATA_PATH+'-{}.csv'.format('CUSTOM'))