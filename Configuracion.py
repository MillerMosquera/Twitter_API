import tweepy
import json

api_key = "pRjSsogC5OIwj5XIPxdUnPTRl"
api_secret = "iKkYxWMKqld5sKI4AjlG2YplPV79t3dogOaixffT2951OrN78i"
baerer_token = r"AAAAAAAAAAAAAAAAAAAAAD2ihQEAAAAA8I9VKK4lMR5mZSOxaB%2FiOTRasSA%3DHueoXaAkrHXuMsdH0rIGzmyHPcBjkqrn5gcmkNjWIEbgCLj94P"
access_token = "1573352412341051392-oYvHNhoQjbHEeSkQz5Fo8LTSrjmeZB"
access_token_secret = "kOLMuFDNzun1PDkCadDXVvpkCju6qB4HakIyEZbBegf0S"


cliente = tweepy.Client(baerer_token, api_key, api_secret,
                        access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


#cliente.create_tweet(text="Hello Twitter")

#print(json.dumps(data._json, indent=2))
