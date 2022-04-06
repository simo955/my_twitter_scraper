import tweepy
from src.config import WANTED_FIELDS, BASIC_DATA_PATH
from src.utils import save_to_df,save_df_to_csv

def getClient(bearer_token):
    return tweepy.Client(bearer_token, wait_on_rate_limit=True, return_type = dict)

def perform_search(client, isUser, user=None, tag=''):
    if isUser and user:
        query='from:{} -is:retweet'.format(user)
    else:
        query='#{}'.format(tag)

    return client.search_recent_tweets(query=query,
                                        tweet_fields=WANTED_FIELDS,
                                        max_results=100)

def build_custom_dt(client, df=None):
    wanted_users = ['elonmusk']
    wanted_hashtags = ['crypto']
    for usr in wanted_users:
        tweets=perform_search(client, True, usr)
        df=save_to_df(tweets['data'], df)
    for tag in wanted_hashtags:
        tweets=perform_search(client, False, tag=tag)
        df=save_to_df(tweets['data'], df)
    
    save_df_to_csv(df, BASIC_DATA_PATH+'-{}.csv'.format('CUSTOM'))