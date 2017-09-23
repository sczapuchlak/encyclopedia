#  --------------------------------------------------------------------------
# Performs a basic keyword search for tweets containing a specific word
# ---------------------------------------------------------------------------

from twitter import *


# Load API Credentials

config = exec(open("config.py").read())


# -----------------------------------------------------------------------
# create twitter API object
# -----------------------------------------------------------------------
twitter = Twitter(auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


# -----------------------------------------------------------------------
# perform a basic search
# Twitter API docs:
# https://dev.twitter.com/rest/reference/get/search/tweets
# -----------------------------------------------------------------------

results = twitter.search.tweets(raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")

# query = twitter.search.tweets(q = "lazy dog")

# -----------------------------------------------------------------------
# How long did this query take?
# -----------------------------------------------------------------------
# print ("Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

# -----------------------------------------------------------------------
# Loop through each of the results, and print its content.
# -----------------------------------------------------------------------
# for result in results["statuses"]:
# print ("(%s) @%s %s" % (results["created_at"], results["user"]["screen_name"], results["text"]))

# search = input("Insert your keyword here:")


# print(results)


