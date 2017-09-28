# Import package to process data
# try: import json
# except ImportError:
#     import simplejson as json

# Import methods from twitter library
from twitter import *
from config import keys

class Requestor():

    def __init__(self):

        # Load API Credentials

        self.ACCESS_KEY = keys.access_key
        self.ACCESS_KEY = keys.access_key
        self.ACCESS_SECRET = keys.access_secret
        self.CONSUMER_KEY = keys.consumer_key
        self.CONSUMER_SECRET = keys.consumer_secret

        # Load API Credentials
        self.oauth = OAuth(self.ACCESS_KEY, self.ACCESS_SECRET, self.CONSUMER_KEY, self.CONSUMER_SECRET)

        # Initiate connection to Twitter API
        self.twitter = Twitter(auth=self.oauth)

def searchTwitter(self, word):

    # A Tweet will be made for each response in searchTwitter(self,word)
    # Tweets will be added to a list and returned

    # -----------------------------------------------------------------------
    # Make outbound request to Twitter & perform a basic search
    # Twitter API docs:
    # https://dev.twitter.com/rest/reference/get/search/tweets
    # -----------------------------------------------------------------------

    # Search tweets for 'word' and return 5
    query = self.twitter.search.tweets(q=word, count=5)

    listOfTweets = []

    # Loop through each of the results, add each status to list
    # https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
    # -----------------------------------------------------------------------
    for result in query["statuses"]:

        # print("(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"]))
        tweet = result
        listOfTweets.append(tweet)

    return listOfTweets


# Testing that everything works as expected...
# requestor = Requestor()
# testString = "cat"
# newlist = searchTwitter(requestor, testString)
# print(newlist)
