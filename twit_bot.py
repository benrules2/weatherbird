import tweepy
from accounts import twitter_account

city_hashtags = {'Toronto':'#torontoweather','Ottawa':'#ottawaweather', 'Montreal':'#mtlweather', "Vancouver":"#vanweather"}

class account:
    def __init__(self):
        consumer_key= twitter_account['consumer_key']
        consumer_secret= twitter_account['consumer_secret']
        access_key = twitter_account['access_key']
        access_secret = twitter_account['access_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)

    def tweet_min_extreme(self, temp, temp_record, city):
        self.api.update_status("{0}'s current temperature of {1} C is below the historic record low of {2} C for this date! #extremeweather {3}".format(city, temp,temp_record, city_hashtags[str(city)]))

    def tweet_max_extreme(self, temp, temp_record, city):
        self.api.update_status("{0}'s current temperature of {1} C is above the historic record high of {2} C for this date! #extremeweather {3}".format(city, temp,temp_record, city_hashtags[str(city)]))

    def tweet_min_avg(self, temp, temp_record, city):
        self.api.update_status("{0}'s current temperature of {1} C is below the historic average low of {2} C for this date! #extremeweather {3}".format(city, temp,temp_record, city_hashtags[str(city)]))

    def tweet_max_avg(self, temp, temp_record, city):
        self.api.update_status("{0}'s current temperature of {1} C is above the historic average high of {2} C for this date! #extremeweather {3}".format(city, temp,temp_record, city_hashtags[str(city)]))

    def test_tweet(self,message):
        self.api.update_status(message)

    def custom_message(self,message):
        self.api.update_status(message)

def combined_less_than_140(message,message_to_add):
    if len(message + message_to_add) <= 140:
        return True
    else:
        return False

def add_if_less_than_140(message, message_to_add):
    if len(message + message_to_add) <= 140:
        return message + message_to_add
    else:
        return message