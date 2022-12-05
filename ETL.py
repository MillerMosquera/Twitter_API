import re
from turtle import pos
import Configuracion
import Conexion
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt


cfg = Configuracion

# public_tweets = cfg.cliente.get_home_timeline()----obtener los publicados y de las personas a las que sigues
# public_tweets = cfg.cliente.search_recent_tweets(query="Programacion")----obtener los de x o y palabra o texto


def ETL():

    # Extraccion
    query = "#reformatributaria "

    tweets = cfg.cliente.search_recent_tweets(query=query,
                                              tweet_fields=[
                                                  'author_id', 'public_metrics', 'created_at', 'source'],
                                              user_fields=[
                                                  "name", "username", "location", "description"],
                                              max_results=100, expansions='author_id',
                                              start_time='2022-10-25T12:00:10Z',
                                              end_time='2022-10-30T18:00:00Z'
                                              )

    tweet_info_ls = []
    # Transformacion
    for tweet, user in zip(tweets.data, tweets.includes['users']):
        tweet_info = {
            'author_id': tweet.author_id,
            'created_at': tweet.created_at,
            'text': tweet.text,
            'source': tweet.source,
            'name': user.name,
            'username': user.username,
            'location': user.location,
            'description': user.description
        }
        tweet_info_ls.append(tweet_info)
    tweets_df = pd.DataFrame(tweet_info_ls)
    tweets_df.head()

    # Valida

    print(tweets_df)

    # Carga a la base de datos

    sql_query = """
    CREATE TABLE IF NOT EXISTS twitter(
        author_id bigint NOT NULL,
        created_at timestamp(6),
        text varchar(250),
        source varchar(200),
        name varchar(200),
        username varchar(200),
        location varchar(200),
        description varchar(250),
        CONSTRAINT primary_key_constraint PRIMARY KEY (author_id)
    )"""
    """
    mycursor = Conexion.mysqldb.cursor()
    mycursor.execute(sql_query)
    print("Opened database successfully")
    
    t
        tweets_df.to_sql("twitter",con = Conexion.engine, index=False, if_exists='append')
    except:
        print("Data already exists in database")
    
    
    print("Closed database")
    """

    def clean_tweet(text):

        return ' '.join(re.sub("(@[A-Za-z0-9]+) | ([^0-9A-Za-z \t]) | (\w+: \/\/\S+)", "", text).split())

    #tweets_list = tweets_df.values.tolist()

    tweets_no_urls = [clean_tweet(tweet.text) for tweet, user in zip(
        tweets.data, tweets.includes['users'])]
    sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_urls]
    sentiment_objects[0].polarity, sentiment_objects[0].subjectivity

    sentiment_values = [[tweet.sentiment.polarity,
                         str(tweet)] for tweet in sentiment_objects]
    sentiment_values[0]

    sentiment_df = pd.DataFrame(
        sentiment_values, columns=["polarity","subjetivity", "tweet"])
    sentiment_df.head()

    print(sentiment_df)
    """"
    print(tweet.text)
    analysis = TextBlob(clean_tweet(tweet.text))
    #analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0] > 0.00:
        print('Positive')
    elif analysis.sentiment[0] < 0.00:
        print('Negative')
    else:
        print('Neutral')

    df = pd.DataFrame()
    # print(tweets_list)
    """
    #tweets_df.to_sql(con=Conexion.engine, name='reforma',if_exists='append', index=False)
ETL()
