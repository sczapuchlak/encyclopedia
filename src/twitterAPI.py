'''Requesting HTTP Resources'''
from twitter import Twitter, OAuth
from os import environ
from config import keys
import wikipedia

class Requestor():
    '''General HTTP Requestor'''

    # Load API Credentials
    ACCESS_KEY = keys.access_key
    ACCESS_SECRET = keys.access_secret
    CONSUMER_KEY = keys.consumer_key
    CONSUMER_SECRET = keys.consumer_secret
    def __init__(self):
        '''Load API Credentials'''

        # Load API Credentials

        self.ACCESS_KEY = keys.access_key
        self.ACCESS_KEY = keys.access_key
        self.ACCESS_SECRET = keys.access_secret
        self.CONSUMER_KEY = keys.consumer_key
        self.CONSUMER_SECRET = keys.consumer_secret



        # Initiate connection to Twitter API
        self.oauth = OAuth(self.ACCESS_KEY, self.ACCESS_SECRET, self.CONSUMER_KEY, self.CONSUMER_SECRET)
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
        query = self.twitter.search.tweets(q=word, count=2)
        list_of_tweets = []
        # Loop through each of the results, add each status to list
        # https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
        # -----------------------------------------------------------------------
        for result in query["statuses"]:
            tweet = result
            list_of_tweets.append(tweet)



        # templateData = {
        #
        #     'tweets': query.get('statuses')
        # }
        #
        # return render_template('search.html', **templateData)

        #return list_of_tweets

        return query





# Testing that everything works as expected...
# requestor = Requestor()
# testString = "cat"
# newlist = requestor.search_twitter(testString)
# print(newlist)