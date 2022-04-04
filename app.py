import tweepy

from src.streamingListener import myStreamListener
from src.keys import bearer
from src.utils import WANTED_FIELDS

def getClient(bearer_token):
    return tweepy.Client(bearer_token, wait_on_rate_limit=True)

def perform_search(client):
    # Replace with your own search query
    query = 'from:elonmusk -is:retweet'
    tweets = client.search_recent_tweets(query=query,
                                        tweet_fields=['context_annotations', 'created_at'],
                                        max_results=10)

    for tweet in tweets.data:
        print(tweet.text)
        if len(tweet.context_annotations) > 0:
            print(tweet.context_annotations)
    return tweets


if __name__ == '__main__':
    # client = getClient(bearer)
    # search_result = perform_search(client)
    # save_to_df(search_result)
    print('Initializing stream..')
    client = myStreamListener(bearer)
    print('Stream initialized. Now running!!')
    client.sample(tweet_fields= WANTED_FIELDS)
    