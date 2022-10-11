import Configuracion
import Conexion
import pandas as pd


cfg = Configuracion

# public_tweets = cfg.cliente.get_home_timeline()----obtener los publicados y de las personas a las que sigues
# public_tweets = cfg.cliente.search_recent_tweets(query="Programacion")----obtener los de x o y palabra o texto


def ETL():

    # Extraccion
    query = "#python"

    tweets = cfg.cliente.search_recent_tweets(query=query, tweet_fields=['author_id', 'public_metrics', 'created_at', 'source'], user_fields=[
        "name", "username", "location", "description"],
        max_results=100, expansions='author_id',
        start_time='2022-10-04T12:00:10Z',
        end_time='2022-10-10T18:00:00Z'
    )

    tweet_info_ls = []
    # Transformacion
    for tweet, user in zip(tweets.data, tweets.includes['users']):
        tweet_info = {
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
    print(tweets_df)

    # Carga a la base de datos
    tweets_df.to_sql(con=Conexion.engine, name='prueba',
                     if_exists='append', index=False)


ETL()
