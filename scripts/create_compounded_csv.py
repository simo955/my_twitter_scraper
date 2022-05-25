import os
import json
import pandas as pd

DATA_PATH=os.environ.get('DATA_PATH', '../data')
DESTIONATION_NAME=os.environ.get('DESTIONATION_NAME', 'destination')
destination_path=DATA_PATH+'/'+DESTIONATION_NAME

def create_compounded_csv(files):
    compounded_df = pd.DataFrame(columns=['id','text','author_id','created_at','public_metrics','lang','geo'])
    
    for path in files:
        file_path=destination_path+'/'+path
        try:
            dt = pd.read_csv(file_path, dtype={'id':str,'text':str, 'author_id':str})
            os.remove(file_path)
        except:
            print('Unable to read:', file_path)
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
    files =  [f for f in os.listdir(destination_path) if '.csv' in f]

    dt = create_compounded_csv(files)

    dt=dt.drop_duplicates(subset=['id'], keep='first')
    dt=create_dummy_columns(dt)

    dt.to_csv(destination_path+'/'+'compounded_df.csv',index=False)