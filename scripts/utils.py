import pandas as pd
import numpy as np
import json


def create_compounded_csv(num_csv=10, basic_path='../data'):
    compounded_df = pd.DataFrame(columns=['id','text','author_id','created_at','public_metrics','lang','geo'])

    for i in range(0, num_csv+1):
        pathname = basic_path+'/tweets-{}.csv'.format(i)
        try:
            dt = pd.read_csv(pathname, dtype={'id':str,'text':str, 'author_id':str})
        except:
            print('Unable to read:', pathname)
            continue
        compounded_df = pd.concat([dt,compounded_df] , ignore_index=True)
        print('New df is now long: {}'.format(compounded_df.shape[0]))
        
    compounded_df=compounded_df.drop_duplicates(subset=['id'], keep='first')
    compounded_df=compounded_df.dropna(subset=['id','text','created_at', 'public_metrics', 'lang'])
    compounded_df['public_metrics']=compounded_df['public_metrics'].str.replace("'", '"')
    compounded_df.reset_index(drop=True, inplace=True)

    return compounded_df


def create_dummy_columns(dt, column_name='public_metrics'):
    dicts=[json.loads(x) for x in dt[column_name].values]
    dt['retweet_count']=[x['retweet_count'] for x in dicts]
    dt['reply_count']=[x['reply_count'] for x in dicts]
    dt['like_count']=[x['like_count'] for x in dicts]
    dt['quote_count']=[x['quote_count'] for x in dicts]
    return dt.drop(columns=['public_metrics'])


if __name__ == "__main__":
    dt1 = create_compounded_csv(num_csv=38,basic_path='../data')
    dt2 = create_compounded_csv(num_csv=38,basic_path='../data1')
    dt3 = create_compounded_csv(num_csv=38,basic_path='../data2')

    dt = pd.concat([dt1, dt2, dt3], ignore_index=True)
    dt=dt.drop_duplicates(subset=['id'], keep='first')
    dt=create_dummy_columns(dt)

    dt.to_csv('compounded_df.csv',index=False)