import tweepy
from src.utils import save_to_df, save_df_to_csv
from src.config import ENG_TEXT, BATCH_SIZE, TOT_TWEET

class myStreamListener(tweepy.StreamingClient):
    total_number_of_tweets = 0
    current_number_batched = 0
    batched_tweets = []
    closed_peacefully = False

    def __init__(self, bearer_token) -> None:
        self.df = None
        super().__init__(bearer_token, wait_on_rate_limit=True, return_type = dict )

    def reset_batch(self):
        self.batched_tweets = []
        self.current_number_batched = 0

    def on_tweet(self, tweet):
        if tweet['lang'] != ENG_TEXT:
           return

        # Exclude retweets, too many mentions
        text = tweet['text']
        if any(('RT @' in text, 'RT' in text, text.count('@') >= 2)):
            return
        
        try:
            self.batched_tweets.append(tweet)
            self.total_number_of_tweets += 1
            self.current_number_batched += 1

            if self.current_number_batched > BATCH_SIZE:
                print('{} tweet parsed'.format(self.total_number_of_tweets))
                self.df = save_to_df(self.batched_tweets, self.df)
                self.reset_batch()

            if self.total_number_of_tweets > TOT_TWEET:
                save_df_to_csv(self.df, 'data/tweets.csv')
                self.closed_peacefully=True
                self.disconnect() 
        
        except Exception as e:
            print('Encountered Exception:', e)
            pass

    def on_errors(self, errors) :
        save_df_to_csv(self.df, 'tweets-{}.csv'.format('BACKUP'))
        print(errors)

    def on_exception(self, e):
        print('on_exception: Encountered Exception:', e)


    def on_disconnect(self):
        if not self.closed_peacefully:
            save_df_to_csv(self.df, 'tweets-{}.csv'.format('BACKUP'))
        print('on disconnect')