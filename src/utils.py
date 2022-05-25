import logging
import pandas as pd

from src.config import WANTED_FIELDS, ENG_TEXT

def save_to_df(results, df):
    if df is None:
        df = pd.DataFrame([], columns=WANTED_FIELDS)

    formatted_results = []
    for tweet in results:
        formatted_results.append( \
            {'id': tweet['id'], \
            'text': tweet['text'], \
            'author_id': tweet['author_id'], \
            'created_at': tweet['created_at'], \
            'public_metrics': tweet['public_metrics'], \
            'lang': tweet['lang'] \
            })
    return df.append(formatted_results)

def save_df_to_csv(df, path, index=False):
    try:
        df.to_csv(path, index=index)
        logging.info('DF saved on {}'.format(path))
    except Exception as e:
        logging.error('Something went wrong while saving the DF. Exception {}'.format(e))

def is_retweet(text):
    if any(('RT' in text, text.count('@') >= 2)):
        return True
    return False

def is_tweet_valid(tweet):
    if  not tweet.get('id') or not tweet.get('text'):
        return False
    if tweet.get('lang') != ENG_TEXT:
        return False
    if is_retweet(tweet.get('text')):
        return False
    return True