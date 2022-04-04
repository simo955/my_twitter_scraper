import os

from src.streamingListener import myStreamListener
from src.utils import WANTED_FIELDS
#from src.keys import bearer

if __name__ == '__main__':
    print('Initializing stream..')
    client = myStreamListener(bearer_token=os.environ['TWITTER_BEARER'])
    print('Stream initialized. Now running!!')
    client.sample(tweet_fields=WANTED_FIELDS)
    