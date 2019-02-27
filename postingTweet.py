import twitter.keys
import oauth2
import json
import urllib
import time

twitterConsumer = oauth2.Consumer(twitter.keys.consumerKey, twitter.keys.consumerSecretKey)
twitterToken = oauth2.Token(twitter.keys.tokenKey, twitter.keys.tokenSecretKey)
twitterClient = oauth2.Client(twitterConsumer, twitterToken)

newTweet = urllib.parse.quote(input("Status update: "), safe='')

tweetToReplyIdentifier = '1100519256922472448'
response = twitterClient.request('https://api.twitter.com/1.1/statuses/update.json?status=' + newTweet + '&in_reply_to_status_id=' + tweetToReplyIdentifier, method='POST')

decodedResponseData = json.loads(response[1].decode())

if 'errors' in decodedResponseData:
    errorDescription = decodedResponseData['errors'][0]['message']
    errorCode = decodedResponseData['errors'][0]['code']
    print('### AN ERROR OCURRED ###')
    print('Code: ' + str(errorCode))
    print('Error description: ' + errorDescription)
    print('########################')
else:
    userInfo = decodedResponseData['user']
    userAccountName = userInfo['screen_name']
    print('Tweet posted successfully using account: ' + userInfo['name'] + '(@' + userInfo['screen_name'] + ')')
    print('Accessing twitter search API to retrieve the data for this post...')

    time.sleep(5)
    response = twitterClient.request('https://api.twitter.com/1.1/search/tweets.json?q=' + userAccountName)
    jsonResponse = json.loads(response[1].decode())
    twitterFeedback = jsonResponse['statuses']
    for tweet in twitterFeedback:
        # for key in tweet:
        #     print(key)
        if tweet['user']['screen_name'] == userAccountName:
            print(tweet['text'])
