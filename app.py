import os
from datetime import datetime

from src.tweepy.streamingListener import myStreamListener
from src.tweepy.functions import create_custom_dt, getClient
from src.utils import WANTED_FIELDS

token=os.environ.get('TWITTER_BEARER', 'XX')

if __name__ == '__main__':
    print('Inizialization..')
    today=datetime.today().strftime('%Y_%m_%d_%H_%M')
    saving_path='data/'+today
    os.mkdir(saving_path)
    print("Directory '% s' created" % saving_path)
    
    # client=getClient(bearer_token=token)
    # create_custom_dt(client, BASIC_DATA_PATH=saving_path)

    print('Custom DT saved')

    stream = myStreamListener(bearer_token=token, BASIC_DATA_PATH=saving_path)
    print('Stream initialized. Now running!!')
    stream.sample(tweet_fields=WANTED_FIELDS)
    