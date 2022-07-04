import tweepy
import requests
import time
import random

def queryRepeatedly():
    while True:
        try:
           client = tweepy.Client(consumer_key=' ',consumer_secret='  ',access_token='  ',access_token_secret='  ')
           for i in range(1,99999): #I know this is not a proper loop, but i have no time to edit it. it works tho :)
                response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random") #json server
                json_data = response.json()
                data = json_data['data']
                #print(data[0]['quoteText'])
                hey = data[0]['quoteText']
                tweet = client.create_tweet(text=hey)
                print(tweet)
                time.sleep(30)
        except Exception as e:
            print(e)
            continue
            time.sleep(30)
        time.sleep(30)
a=0
while a <=10:
  queryRepeatedly()
