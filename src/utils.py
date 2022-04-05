import pandas as pd
import tweepy

from src.config import WANTED_FIELDS


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
    
    save_df_to_csv(df, 'data/tweets-SPECIFIC.csv')

def save_to_df(results, df):
    if df is None:
        df = pd.DataFrame([], columns=WANTED_FIELDS)
    formatted_results = []
    for elem in results:
        formatted_results.append( \
            {'id': elem['id'], \
            'text': elem['text'], \
            'author_id': elem['author_id'], \
            'created_at': elem['created_at'], \
            'public_metrics': elem['public_metrics'], \
            'lang': elem['lang'] \
            })

    print('DF UPDATED')
    return df.append(formatted_results)

def save_df_to_csv(df, path, index=False):
    try:
        df.to_csv(path, index=index)
        print('DF Saved on file {}'.format(path))
    except Exception as e:
        print(e, 'Something went wrong while saving the DF on file.')
