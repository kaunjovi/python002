import tweepy
import configparser


# Consumer keys and access tokens, used for OAuth
config = configparser.RawConfigParser()
config.read('secret.properties')

# print config.get('twitterapikeys', 'consumer_key')
# print config.get('twitterapikeys', 'consumer_secret')
# print config.get('twitterapikeys', 'access_token')
# print config.get('twitterapikeys', 'access_token_secret')

consumer_key = config.get('twitterapikeys', 'consumer_key')
consumer_secret = config.get('twitterapikeys', 'consumer_secret')
access_token = config.get('twitterapikeys', 'access_token')
access_token_secret = config.get('twitterapikeys', 'access_token_secret')

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Creates the user object. The me() method returns the user
user = api.me()

print 'Name: ' + user.name
print 'Location: ' + user.location
print 'Friends: ' + str(user.friends_count)

# Read the timeline. Read only 10 at a time.
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print status.text.encode('utf-8')

# Who all are our friends on twitter
for friend in tweepy.Cursor(api.friends).items():
    print friend.name

# A list of my tweets.
for tweet in tweepy.Cursor(api.user_timeline).items(10):
  print tweet.text
