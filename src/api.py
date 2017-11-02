from twitter import Twitter, OAuth
import safygiphy
from os import environ
import wikipedia


class Result:
    def __init__(self):
        self.tweets = list()
        self.gifs = list()
        self.articles = list()
    def __repr__(self):
        return 'tweets:\n{tw}\n\ngifs:\n{gf}\n\narticles:\n{ar}'\
        .format(tw=self.tweets, gf=self.gifs, ar=self.articles)

class Requestor:

    def __init__(self):
        '''All API Credentials (Twitter, Giphy, Flickr)'''

        '''Load Twitter API Credentials'''
        self.oauth = OAuth(environ.get('twitter_access_key'),\
        environ.get('twitter_access_secret'), environ.get('twitter_consumer_key'),\
        environ.get('twitter_consumer_secret'))
        '''Initiate connection to Twitter API'''
        self.twitter = Twitter(auth=self.oauth)

        '''Load Giphy API Key'''
        self.token = environ.get('giphy_access_key')

    def search_twitter(self, word):
        '''A Tweet will be made for each response in searchTwitter(self,word)
        Tweets will be added to a list and returned
        -----------------------------------------------------------------------
        Make outbound request to Twitter & perform a basic search
        Twitter API docs:
        https://dev.twitter.com/rest/reference/get/search/tweets
        -----------------------------------------------------------------------
        Search tweets for 'word' and return 10'''
        query = self.twitter.search.tweets(q=word, count=10)
        return query['statuses']

    def search_giphy(self, word):
        '''search for gifs on giphy'''
        '''
            -----------------------------------------------------------------------
            Make outbound request to Giphy & perform a basic search

            - Returns list of 10 iframes containing gifs (to embed gif)
            
            NOTE: If you want the Gif ID returned instead of iframe,
            change line 67 to read:
            list_of_gifs.append(results)
            -----------------------------------------------------------------------
            References:
            https://github.com/StewPoll/safygiphy
            https://developers.giphy.com/docs/
            -----------------------------------------------------------------------
        '''
        # Should have dashes and not spaces
        if word:
            word = word.replace(' ', '-')
        # New Request Object with API Credentials
        giphy = safygiphy.Giphy(token=self.token)
        # To hold return results
        list_of_gifs = []

        # Prefix/Suffix to Embed the results
        prefix = """<iframe src="https://giphy.com/embed/"""
        suffix = """" width="360" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>"""
        # Produce collection of 10 iframes containing gifs @ random by search word
        for i in range(10):
            results = giphy.random(tag=word)["data"]["id"]
            embed_gifs = prefix + results + suffix
            # print(embed_gifs) this was to make sure correct syntax
            list_of_gifs.append(embed_gifs)

        return list_of_gifs

    def search_wiki(self, word):

        # Searches Wikipedia for word and returns summary of that page
        try:
            summary = wikipedia.summary(word)
            
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            summary = ['Unable to find info on {w}'.format(w=word),'did you mean one of these?']
            summary.extend(e.options)
        return summary
