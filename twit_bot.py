import tweepy
from accounts import twitter_account

city_hashtags = {'Toronto':'#torontoweather','Ottawa':'#ottawaweather', 'Montreal':'#mtlweather', "Vancouver":"#vanweather"}

class account:
    def __init__(self, city_name):
        consumer_key= twitter_account[str(city_name)]['consumer_key']
        consumer_secret= twitter_account[str(city_name)]['consumer_secret']
        access_key = twitter_account[str(city_name)]['access_key']
        access_secret = twitter_account[str(city_name)]['access_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)

    def tweet_min_extreme(self, temp, temp_record, city):
        message = "{0}'s current temperature of {1}°C is {2}°C below the record low of {3}°C for this date! #extremeweather {4}".format(city, temp, round(abs(temp - temp_record),1), temp_record, city_hashtags[str(city)])
        print(message)
        self.custom_message(message)

    def tweet_max_extreme(self, temp, temp_record, city):
        message = "{0}'s current temperature of {1}°C is {2}°C above the record high of {3}°C for this date! #extremeweather {4}".format(city, temp, round(abs(temp - temp_record),1), temp_record, city_hashtags[str(city)])
        print(message)
        self.custom_message(message)

    def tweet_min_avg(self, temp, temp_record, city):
        message = "{0}'s current temperature of {1}°C is {2}°C below the average low of {3}°C for this date! #extremeweather {4}".format(city, temp, round(abs(temp - temp_record),1), temp_record, city_hashtags[str(city)])
        print(message)
        self.custom_message(message)

    def tweet_max_avg(self, temp, temp_record, city):
        message = "{0}'s current temperature of {1}°C is {2}°C above the average high of {3}°C for this date! #extremeweather {4}".format(city, temp, round(abs(temp - temp_record),1), temp_record, city_hashtags[str(city)])
        print(message)
        self.custom_message(message)

    def test_tweet(self,message):
        self.api.update_status(message)

    def custom_message(self,message):
        self.api.update_status(message)

    def tweet_message_with_photo(self, message, file_filename, city_name):
        message += ' ' + city_hashtags[str(city_name)]
        self.api.update_with_media(file_filename,message)

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