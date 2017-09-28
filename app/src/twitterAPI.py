'''Requesting HTTP Resources'''
from twitter import Twitter, OAuth
from os import environ

class Requestor():
    '''General HTTP Requestor'''
    def __init__(self):
        '''Load API Credentials'''

        # Load API Credentials
        self.oauth = OAuth(environ.get('twitter_access_key'),\
        environ.get('twitter_access_secret'), environ.get('twitter_consumer_key'),\
        environ.get('twitter_consumer_secret'))
        # Initiate connection to Twitter API
        self.twitter = Twitter(auth=self.oauth)
    def search_twitter(self, word):
        '''A Tweet will be made for each response in searchTwitter(self,word)
        Tweets will be added to a list and returned
        -----------------------------------------------------------------------
        Make outbound request to Twitter & perform a basic search
        Twitter API docs:
        https://dev.twitter.com/rest/reference/get/search/tweets
        -----------------------------------------------------------------------
        Search tweets for 'word' and return 5'''
        query = self.twitter.search.tweets(q=word, count=5)
        list_of_tweets = []
        # Loop through each of the results, add each status to list
        # https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
        # -----------------------------------------------------------------------
        for result in query["statuses"]:
            tweet = result
            list_of_tweets.append(tweet)
        return list_of_tweets
