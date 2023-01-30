from os import getenv
import random
import datetime
from time import sleep

from dotenv import load_dotenv
import tweepy
from flask import Flask


emojis = [
    '\U0001F300', '\U0001F320',
    '\U0001F330', '\U0001F335',
    '\U0001F337', '\U0001F37C',
    '\U0001F380', '\U0001F393',
    '\U0001F3A0', '\U0001F3C4',
    '\U0001F3C6', '\U0001F3CA',
    '\U0001F3E0', '\U0001F3F0',
    '\U0001F400', '\U0001F43E',
    '\U0001F440', '\U0001F442',
    '\U0001F4F9', '\U0001F4FC',
    '\U0001F500', '\U0001F53C',
    '\U0001F540', '\U0001F543',
    '\U0001F550', '\U0001F567',
    '\U0001F5FB', '\U0001F5FF',
    '\U0001F300', '\U0001F32C',
    '\U0001F330', '\U0001F37D',
    '\U0001F380', '\U0001F3CE',
    '\U0001F3D4', '\U0001F3F7',
    '\U0001F400', '\U0001F4FE',
    '\U0001F500', '\U0001F54A',
    '\U0001F550', '\U0001F579',
    '\U0001F57B', '\U0001F5A3',
    '\U0001F5A5', '\U0001F5FF',
    '\U0001F300', '\U0001F579',
    '\U0001F57B', '\U0001F5A3',
    '\U0001F5A5', '\U0001F5FF',
    '\U0001F4F7'
]


app = Flask(__name__)

@app.route('/')
def index():
    load_dotenv()

    API_KEY = getenv('API_KEY')
    API_KEY_SECRET = getenv('API_KEY_SECRET')
    ACCESS_TOKEN = getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = getenv('ACCESS_TOKEN_SECRET')

    if not API_KEY or not API_KEY_SECRET or not ACCESS_TOKEN or not ACCESS_TOKEN_SECRET:
        raise ValueError('Missing environment variables')

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    while True:
        if datetime.datetime.now().hour == 12 and datetime.datetime.now().minute == 15:
            try:
                remaining_days = datetime.date(
                    2023, 6, 30) - datetime.date.today()

                swearing = [' caraio', ' pqp', ' porra',
                            ', num guento mais', ' bucetaaaaaaaa', ', ovo chora 😭']

                tweet = f'{remaining_days.days} dias faltando, vai logo' + \
                    random.choice(swearing) + ' ' + \
                    random.choice(emojis)

                api.update_status(tweet)
                print(tweet)
            except Exception as error:
                print(error)
                break

        sleep(45)

    return 'férias, pqp!'

if __name__ == '__main__':
    app.run(
      host='0.0.0.0',
      port=3000
    )
