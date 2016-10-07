import os
import urllib2 as urllib
from toolz import interpose

import oauth2 as oauth

TW_ACCESS_KEY = os.environ["twitter_access_token_key"]
TW_SECRET = os.environ["twitter_access_token_secret"]
NT_API_KEY = os.environ["nu_twitter_api_key"]
NT_API_SECRET = os.environ["nu_twitter_api_secret"]

OAUTH_TOKEN = oauth.Token(key=TW_ACCESS_KEY, secret=TW_SECRET)
OAUTH_CONSUMER = oauth.Consumer(key=NT_API_KEY, secret=NT_API_SECRET)
SIGNATURE_METHOD = oauth.SignatureMethod_HMAC_SHA1()

HTTP_METHOD = 'GET'
HTTP_HANDLER = urllib.HTTPHandler(debuglevel=0)
HTTPS_HANDLER = urllib.HTTPSHandler(debuglevel=0)

URL_QUERY = "https://api.twitter.com/1.1/search/tweets.json"

BOOTSTRAP_ID = 721267742230323200
SCHEMA_TWEETS = '(id INTEGER PRIMARY KEY, time DATETIME, user_id INT, account_since DATETIME, ' \
                'friends_count INT, followers_count INT, location TEXT, text_tweet TEXT, consult TEXT)'
LIST_COLUMNS_TWEET = ['id', 'time', 'user_id', 'account_since', 'friends_count', 'followers_count', 'location',
                      'text_tweet', 'consult']
STRING_COLUMNS_TWEET = '(' + ''.join(interpose(',', LIST_COLUMNS_TWEET)) + ')'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_ENV = 'test'
DATA_STORAGE_PATH = os.path.join((os.sep).join(BASE_DIR.split(os.sep)[0:-2]), 'data')
DATA_STORAGE_DIR = os.path.join(DATA_STORAGE_PATH, 'storage/test/raw_tweets/') if TEST_ENV \
                                else os.path.join(DATA_STORAGE_PATH, 'storage/prod/raw_tweets/')


KEY_WORDS = {'nubank': ['nubank', 'nubankbrasil', 'sounu', 'nulove'],
             'itau': ['itau', 'issomudaomundo'],
             'bradesco': ['bradesco'],
             'digio': ['meudigio'],
             'original': ['bancooriginal', 'souoriginal'],
             'brasil': ['bancodobrasil'],
             'caixa': ['caixa']}

