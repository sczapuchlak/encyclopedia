# Import package to process data
# try: import json
# except ImportError:
#     import simplejson as json

# Import methods from twitter library
from twitter import *
from config import keys


# Load API Credentials
ACCESS_KEY = keys.access_key
ACCESS_SECRET = keys.access_secret
CONSUMER_KEY = keys.consumer_key
CONSUMER_SECRET = keys.consumer_secret

oauth = OAuth(ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate connection to Twitter API

twitter = Twitter(auth=oauth)

# -----------------------------------------------------------------------
# perform a basic search
# Twitter API docs:
# https://dev.twitter.com/rest/reference/get/search/tweets
# -----------------------------------------------------------------------

def search(word):

    # search with query term and return 5

    query = twitter.search.tweets(q=word, count=5)

    return query
# -----------------------------------------------------------------------
# Loop through each of the results, and print its content.
# -----------------------------------------------------------------------

testString = "cats"

results = search(testString)

# for result in results["statuses"]:
#     print("(%s) @%s %s" % (results["created_at"], results["user"]["screen_name"], results["text"]))


print(results)

