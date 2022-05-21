import os
import json
import shutil
import pandas as pd

data_path='destination'

def unpack_downloaded_data():
    dirs = [d for d in os.listdir() if '.' not in d]
    dest_dir='destination/'

    try: 
        os.mkdir(dest_dir) 
        print('Created destination repo {}!'.format(dest_dir))
    except OSError as error: 
        print(error)


    for d in dirs:
        error_flag=0
        files = [f.split('.csv')[0] for f in os.listdir(d) if '.csv' in f]
    
        print('In directory {} found files: {}'.format(d, files))
        for f in files:
            original_path = d+'/'+f+'.csv'
            new_path = dest_dir+f+'_'+d+'.csv'
            try:
                #Move file to new path
                os.rename(original_path, new_path)
            except Exception as e:
                print('Unable to move file. Exception', e)
                error_flag=1
        
        if error_flag==0:
        #Delete repository
            try:
                print('Removing {} directory'.format(d))
                shutil.rmtree(d)
            except OSError as e:
                print("Error: %s : %s" % (d, e.strerror))

def create_compounded_csv(files):
    compounded_df = pd.DataFrame(columns=['id','text','author_id','created_at','public_metrics','lang','geo'])
    
    for path in files:
        try:
            dt = pd.read_csv(data_path+'/'+path, dtype={'id':str,'text':str, 'author_id':str})

        except:
            print('Unable to read:', path)
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
    files =  [f for f in os.listdir(data_path) if '.csv' in f]

    dt = create_compounded_csv(files)

    dt=dt.drop_duplicates(subset=['id'], keep='first')
    dt=create_dummy_columns(dt)

    dt.to_csv('compounded_df.csv',index=False)