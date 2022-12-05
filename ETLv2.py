from multiprocessing.sharedctypes import Value
import json
import tweepy
import sys
import Conexion as conn
import Configuracion as config
import time
import pandas as pd


search_terms = ["python", "bigdata", "programming", "coding"]


class MyStream(tweepy.StreamingClient):

    def on_data(self, data):

        all_data = json.loads(data)
        print(all_data)

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            # print(tweet)
            time.sleep(0.2)

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)


if (not config.api):
    print("Falla en la Auntenticación")
    sys.exit(-1)

stream = MyStream(config.baerer_token)

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets",
              'author_id', 'created_at', 'source'], user_fields=[
    "name", "username", "location", "description"], expansions='author_id')
#stream.filter(track=["Python"], languages=["en"])
