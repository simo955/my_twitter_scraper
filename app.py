import os

from src.tweepy.streamingListener import myStreamListener
from src.tweepy.functions import build_custom_dt, getClient
from src.utils import WANTED_FIELDS

token=os.environ['TWITTER_BEARER']

if __name__ == '__main__':
    print('Inizialization..')
    client=getClient(bearer_token=token)
    build_custom_dt(client)

    print('Specific dt created')

    stream = myStreamListener(bearer_token=token)
    print('Stream initialized. Now running!!')
    stream.sample(tweet_fields=WANTED_FIELDS)
    