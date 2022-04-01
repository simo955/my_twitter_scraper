import tweepy
import pandas as pd

from streamingListener import myStreamListener
from keys import bearer

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
    df = pd.DataFrame([], columns=['text', 'author_id', 'created_at'])

    client = myStreamListener(bearer, df )
    client.sample(tweet_fields=['author_id', 'lang', 'created_at'])
    