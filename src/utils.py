import pandas as pd
import tweepy

from src.config import WANTED_FIELDS

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

def is_retweet(text):
    if any(('RT @' in text, 'RT' in text, text.count('@') >= 2)):
        return True
    return False