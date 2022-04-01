import pandas as pd

def save_to_df(results, df):
    # TODO: if df is None: crea df
    formatted_results = []
    for elem in results:
        formatted_results.append( \
            {'text': elem['text'], \
            'author_id': elem['author_id'], \
            'created_at': elem['created_at'] \
            })

    return df.append(formatted_results)

def save_df_to_csv(df, path, index=False):
    try:
        df.to_csv(path, index=index)
    except Exception as e:
        print(e, 'Something went wrong while saving')


# df = pd.DataFrame([['text1', 'author1', 'created at 1'], ['text2', 'author1', 'created at 2']], columns=['text', 'author_id', 'created_at'])
# results = [{'text': 'text3', 'author_id': 'auth2', 'created_at': 'created at 3'}]
# df = save_to_df(results, df)
# save_df_to_csv(df, 'tweets.csv')
