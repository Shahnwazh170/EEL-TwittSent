import tweepy
from textblob import TextBlob
from nltk.corpus import stopwords
from string import punctuation
import re
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import eel

eel.init('../gui')

api_key = "zAd6YfgCEmQrtUYon6WpTCbFr"
api_secret_key = "zqiwFkZrHtvBN2a34ADb0EqDDfwtnTl4tLm1zWfGciYb1aXwsc"
access_token = "922295559053905920-Nmn1kckwIQwRWnhQ6avAzOgnG0InKGG"
access_token_secret = "YtirfOBSgpyBvFBYDtN7VcX3F2dwOP084rl1QCN1SFL5I"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class DataPreProcessing:

    def __init__(self, raw_tweet_data):
        self.raw_tweet_data = raw_tweet_data
        self.stopwords = set(stopwords.words("english") + list(punctuation))

    def process_tweet(self, tweet):
        tweet = tweet.lower()
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet)  # remove URLs
        tweet = re.sub('@[^\s]+', "", tweet)  # remove usernames
        tweet = re.sub(r'#([^\s]+)', "", tweet)
        try:
            if TextBlob(tweet).detect_language() != "en":
                tweet = self.translate_tweet(tweet)
        except:
            pass

        temp = ""
        for i in word_tokenize(tweet):
            if i not in self.stopwords:
                temp += i + " "
        return temp

    def translate_tweet(self, tweet):

        return TextBlob(tweet).translate(to="en").raw

    def process_all_tweets(self):

        tweet_data = []
        for i in self.raw_tweet_data:
            tweet_data.append(self.process_tweet(i))
        return tweet_data


def fetch_tweets(keyword, count):
    return [tweet.text for tweet in api.search(keyword, count=count)]


def get_sentiment(tweets_data):
    polarity = []
    for tweet in tweets_data:
        s = TextBlob(tweet)
        polarity.append(s.sentiment.polarity)
    return polarity


@eel.expose
def main(keyword, number):
    raw_tweets = fetch_tweets(keyword, number)

    processor = DataPreProcessing(raw_tweets)
    processed_data = processor.process_all_tweets()

    polarity = get_sentiment(processed_data)

    max_polarity = max(polarity)
    max_index = polarity.index(max_polarity)

    min_polarity = min(polarity)
    min_index = polarity.index(min_polarity)

    highly_pos = (max_polarity, raw_tweets[max_index])
    highly_neg = (min_polarity, raw_tweets[min_index])

    pos_polarity, neg_polarity, neu_polarity = divide_polarity(polarity)

    result_dict = {
        "polarity": polarity,
        "highly_pos": highly_pos,
        "highly_neg": highly_neg,
        "pos_polarity": pos_polarity,
        "neg_polarity": neg_polarity,
        "neu_polarity": neu_polarity
    }
    return result_dict


def divide_polarity(polarity):
    pos_polarity = []
    neg_polarity = []
    neu_polarity = 0
    for i in polarity:
        if i > 0:
            pos_polarity.append(i)
        elif i < 0:
            neg_polarity.append(i)
        else:
            neu_polarity += 1

    return pos_polarity, neg_polarity, neu_polarity


eel.start("index.html", size=(900, 720))
