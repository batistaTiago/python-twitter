import pprint

import twitter.keys
import oauth2
import json
import urllib

twitterConsumer = oauth2.Consumer(twitter.keys.consumerKey, twitter.keys.consumerSecretKey)
twitterToken = oauth2.Token(twitter.keys.tokenKey, twitter.keys.tokenSecretKey)
twitterClient = oauth2.Client(twitterConsumer, twitterToken)

rawQuery = input("Pesquise: ")
query = urllib.parse.quote(rawQuery, safe='')

response = twitterClient.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query)

jsonResponse = json.loads(response[1].decode())

tweets = jsonResponse['statuses']  # statuses returns a list of tweets
#  tweet = tweets[0]  # first tweet of the list
#  print(tweet['entities'])  # hashtags, mentions, urls and symbols

# for tweet in tweets:
#     for key in tweet:
#         print(key)
#     if tweet['user']['screen_name'] == rawQuery:
#         if tweet['text'] == 'teste no python':
#             print('achado automatico')
#             print(tweet['source'])
#         elif tweet['text'] == 'teste na mao':
#             print('achado na mao')
#             print(tweet['source'])


for tweet in tweets:
    print(tweet['user']['screen_name'])
    print(tweet['text'])
    print(tweet['id'])
    print()
