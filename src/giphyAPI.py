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
        '''search for gifs on giphy'''
        '''
            -----------------------------------------------------------------------
            Make outbound request to Giphy & perform a basic search

            - Returns list of 10 iframes containing gifs (to embed gif)
            
            NOTE: If you want the Gif ID returned instead of iframe,
            change line 67 to read:
            list_of_gifs.append(results)
            -----------------------------------------------------------------------
            Refrences:
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


# https://github.com/StewPoll/safygiphy
# https://developers.giphy.com/docs/



#print(newlist)



