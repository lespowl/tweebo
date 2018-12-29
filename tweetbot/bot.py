import tweepy

from secrets import *

#create OAuthHandler Instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

#construct API instance
api = tweepy.API(auth)

user = api.get_user('lespowl')
for friend in user.friends():
   print("- " + friend.screen_name)
