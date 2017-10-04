'''Requesting HTTP Resources'''
import safygiphy
from os import environ
#from config import giphyKeys

class Giphy(object):
    '''Object that handles making GIF related calls'''

    def __init__(self):
        '''Load API Key'''
        self.token = environ.get('giphy_access_key')

        # testing locally
        # self.token = giphyKeys.giphy_key


def search_giphy(self, word):
    '''
    -----------------------------------------------------------------------
    Make outbound request to Giphy & perform a basic search
    -----------------------------------------------------------------------
    '''
    # Should have dashes and not spaces
    if word:
        word = word.replace(' ', '-')

    giphy = safygiphy.Giphy(token=self.token)

    # Will return a random GIF with tag "word"
    results = giphy.random(tag=word)

    return results


# # Testing
# g = Giphy()
# word = "funny cat"
# q = search_giphy(g, word)
# print(q)

''' 
https://github.com/StewPoll/safygiphy 
https://developers.giphy.com/docs/
'''