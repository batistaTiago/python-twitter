import pprint
import twitter.keys
import oauth2
import json
import urllib
import time

targetTweetId = '1100431560078180352'

twitterConsumer = oauth2.Consumer(twitter.keys.consumerKey, twitter.keys.consumerSecretKey)
twitterToken = oauth2.Token(twitter.keys.tokenKey, twitter.keys.tokenSecretKey)
twitterClient = oauth2.Client(twitterConsumer, twitterToken)

response = twitterClient.request('https://api.twitter.com/1.1/statuses/retweet/' + targetTweetId + '.json',
                                 method='POST')

