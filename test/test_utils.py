import unittest
from src.utils import is_retweet, is_tweet_valid

class TestUtils(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_is_retweet(self):
        self.assertEqual(is_retweet('RT @blabla bla '), True)
        self.assertEqual(is_retweet('bla blaRTbla bla '), True)
        self.assertEqual(is_retweet('prova@.it RT@bla bla'), True)
        self.assertEqual(is_retweet(''), False)
        self.assertEqual(is_retweet('bla bla bla'), False)

    def test_is_tweet_valid(self):
        self.assertEqual(is_tweet_valid({}), False)
        self.assertEqual(is_tweet_valid({'id':1}), False)
        self.assertEqual(is_tweet_valid({'text':'bla'}), False)
        self.assertEqual(is_tweet_valid({'id':1, 'text':'bla'}), False)
        self.assertEqual(is_tweet_valid({'id':1, 'text':'bla', 'lang': 'not en'}), False)
        self.assertEqual(is_tweet_valid({'id':1, 'text':'RT', 'lang': 'en'}), False)
        self.assertEqual(is_tweet_valid({'id':1, 'text':'bla', 'lang': 'en'}), True)




