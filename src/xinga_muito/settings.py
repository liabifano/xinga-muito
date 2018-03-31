import os

import oauth2 as oauth
from toolz import interpose
from urllib.request import HTTPHandler, HTTPSHandler

TW_ACCESS_KEY = os.environ["twitter_access_token_key"]
TW_SECRET = os.environ["twitter_access_token_secret"]
NT_API_KEY = os.environ["nu_twitter_api_key"]
NT_API_SECRET = os.environ["nu_twitter_api_secret"]

OAUTH_TOKEN = oauth.Token(key=TW_ACCESS_KEY, secret=TW_SECRET)
OAUTH_CONSUMER = oauth.Consumer(key=NT_API_KEY, secret=NT_API_SECRET)
SIGNATURE_METHOD = oauth.SignatureMethod_HMAC_SHA1()

HTTP_METHOD = 'GET'
HTTP_HANDLER = HTTPHandler(debuglevel=0)
HTTPS_HANDLER = HTTPSHandler(debuglevel=0)

URL_QUERY = "https://api.twitter.com/1.1/search/tweets.json"
SLEEP_TIME_REQUESTS = 20

BOOTSTRAP_ID = 979716455674601474

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV = 'test'
DATA_STORAGE_PATH = os.path.join((os.sep).join(BASE_DIR.split(os.sep)[0:-2]), 'data/storage/')
DATA_STORAGE_DIR = os.path.join(DATA_STORAGE_PATH, 'test/') if ENV \
    else os.path.join(DATA_STORAGE_PATH, 'prod/')

KEY_WORDS = {# Biggest ones
             'itau': ['@itau'],
             'brasil': ['@BancodoBrasil'],
             'bradesco': ['@Bradesco'],
             'caixa': ['@Caixa'],
             'bndes': ['@bndes'],
             'santander': ['@santander_br'],
             'banrisul': ['@Banrisul'],
             # 'hsbc': ['@HSBC'] no hsbc for brasil
             # 'citibank': ['@Citibank'], no citibank for brasil
             # Fintechs ones
             'next': ['@falanext'], # bradesco
             'neon': ['@banconeon'],
             'nubank': ['@nubankbrasil'],
             'inter': ['@Bancointer'],
             'digio': ['@meudigio'],
             'original': ['@BancoOriginal'],
             }
