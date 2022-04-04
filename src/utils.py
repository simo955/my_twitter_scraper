import pandas as pd
import tweepy

from src.config import WANTED_FIELDS


def getClient(bearer_token):
    return tweepy.Client(bearer_token, wait_on_rate_limit=True)

def perform_search(client):
    # Replace with your own search query
    query = 'from:elonmusk -is:retweet'
    tweets = client.search_recent_tweets(query=query,
                                        tweet_fields=WANTED_FIELDS,
                                        max_results=10)

    for tweet in tweets.data:
        print(tweet.text)
        if len(tweet.context_annotations) > 0:
            print(tweet.context_annotations)
    return tweets

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
