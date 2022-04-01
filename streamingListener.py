import tweepy

class streamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet)
    
    
    def on_exception(self, exception):
        print(exception, 'EXXXXXX!!!!!!!')