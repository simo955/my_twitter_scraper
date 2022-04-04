import pandas as pd

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


# df = pd.DataFrame([['text1', 'author1', 'created at 1'], ['text2', 'author1', 'created at 2']], columns=['text', 'author_id', 'created_at'])
# results = [{'text': 'text3', 'author_id': 'auth2', 'created_at': 'created at 3'}]
# df = save_to_df(results, df)
# save_df_to_csv(df, 'tweets.csv')
