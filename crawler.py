import os
from datetime import datetime
import logging

from src.tweepy.streamingListener import myStreamListener
from src.tweepy.functions import create_custom_dt, getClient
from src.utils import WANTED_FIELDS

token=os.environ.get('TWITTER_BEARER', 'XX')
today=datetime.today().strftime('%Y_%m_%d_%H_%M')

if __name__ == '__main__':
    logging.info('Initialization..')
    
    saving_path = 'data/' + today
    try:
        os.mkdir(saving_path)
        logging.info('Saving directory {} created'.format(saving_path))
    except Exception as e:
        logging.error('Unable to create saving directory: {}. Exception: {}'.format(saving_path, e))

    # client=getClient(bearer_token=token)
    # create_custom_dt(client, BASIC_DATA_PATH=saving_path)

    stream = myStreamListener(bearer_token=token, BASIC_DATA_PATH=saving_path)
    logging.info('Stream initialized. Now running!!')
    stream.sample(tweet_fields=WANTED_FIELDS)
    