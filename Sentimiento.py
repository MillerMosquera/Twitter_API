import re
import sys
import tweepy
from textblob import TextBlob
import Configuracion as config
import pandas as pd
import Conexion as conexion
import time


engine = conexion.engine
reforma = "SELECT * from reforma"
consulta = pd.read_sql(reforma, con=engine)
consulta.head()

print(consulta)

def clean_text(text):
  text = re.sub(r'^RT[\s]+', '', text)
  text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
  text = re.sub(r'#', '', text)
  text = re.sub(r'@[A-Za-z0-9]+', '', text)
  return text


consulta['clean_text'] = consulta['text'].apply(clean_text)
consulta['clean_text']

print(consulta)


def get_polarity(text):
  analysis = TextBlob(text)
  if text != '':
      result = analysis.translate(from_lang='es', to='en').sentiment.polarity
      return result


consulta['polarity'] = consulta['clean_text'].apply(get_polarity)
consulta['polarity'].head()
print(consulta)

#consulta.to_sql(con=engine, name='opinionreforma',if_exists='append', index=False)

"""""
print(consulta.text)
analysis = TextBlob(str(consulta.text))
#analysis = TextBlob(tweet.text)
print(analysis.sentiment)
if analysis.sentiment[0] > 0.00:
    print('Positive')
elif analysis.sentiment[0] < 0.00:
    print('Negative')
else:
    print('Neutral')

df = pd.DataFrame(analysis.sentiment, columns=['polarity'])

print(df)
"""