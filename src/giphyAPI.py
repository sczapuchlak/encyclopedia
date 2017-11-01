'''Requesting HTTP Resources'''
import safygiphy
from os import environ
import json
from config import giphyKeys

class Giphy(object):
    '''Object that handles making GIF related calls'''
    def __init__(self):
        '''Load API Key'''
        self.token = environ.get('giphy_access_key')
        self.token = giphyKeys.giphy_key
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

        list_of_gifs = []
        #Prefix/Suffix to Embed the results (id of gif)
        prefix = """<iframe src="https://giphy.com/embed/"""
        suffix = """" width="360" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>"""

        for i in range(10):

            results = giphy.random(tag=word)["data"]["id"]
            embed_gifs = prefix + results + suffix
            print(embed_gifs)
            list_of_gifs.append(embed_gifs)

            #If you don't want the iframes attached as a result, I can just return the 'id' for you to enter into a front end iframe
            #by chaging line# to list_of_gifs.append(results)

        return list_of_gifs

# https://github.com/StewPoll/safygiphy
# https://developers.giphy.com/docs/



#print(newlist)



