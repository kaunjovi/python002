import tweepy
 
# Consumer keys and access tokens, used for OAuth
consumer_key = 'km9ZVmO42qCtcjcukbk4B54qS'
consumer_secret = 'NeURzc08wrGhA0emAxpjdJx8MOK4RsyXBDl4VDADQ6rLKTQub6'
access_token = '719722333632643076-4fNGpXADGQgapb1OAk3bMAQRXfNZbqg'
access_token_secret = 'qRwx3YMeIB42iDpInontLtVuMaMnWJTmlr2twOsArbcnc'

 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.me()
 
print 'Name: ' + user.name
print 'Location: ' + user.location
print 'Friends: ' + str(user.friends_count)