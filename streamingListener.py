import tweepy

class myStreamListener(tweepy.StreamingClient):
    total_number_of_tweets = 0
    current_number_batched = 0
    batched_tweets = []

    def __init__(self, bearer, df) -> None:
        self.df = df
        super().__init__(bearer, response_type = dict )

    def on_tweet(self, tweet):
       # TODO: filter per lang 
        self.batched_tweets.append(tweet)
        self.total_number_of_tweets += 1
        self.current_number_batched += 1

        # if self.current_number_batched > 10:
        #     with open('tweets.txt', 'w') as tweetFile:
        #         for record in self.batched_tweets:
        #             tweetFile.write('%s\n' % record)
        #     tweetFile.write('%s\n' % '--------------------------------------------')
        #     self.batched_tweets = []
        #     self.current_number_batched = 0
        
        print(tweet)
        print(tweet.author_id)
        print(tweet.lang)
        print(tweet.created_at)

        print(self.total_number_of_tweets)
        print(self.current_number_batched)
        
    
    
    def on_exception(self, exception):
        print(exception, 'EXXXXXX!!!!!!!')