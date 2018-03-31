import json

import peewee as pw
import requests
from bs4 import BeautifulSoup, element
from dateutil import parser
from w3lib.html import remove_tags

from xinga_muito.settings import DATA_STORAGE_DIR


def get_raw_text(s):
    if isinstance(s, element.Tag):
        s = remove_tags(str(s))

    return '' if str(s).isspace() else str(s)


def parse_one_twitter_output(t):
    if t['truncated']:
        r = requests.get(t['text'].split(' ')[-1])
        soup = BeautifulSoup(r.text, 'html5lib')
        list_text = soup.find('p', class_='TweetTextSize TweetTextSize--jumbo js-tweet-text tweet-text').contents
        list_text = [get_raw_text(x) for x in list_text]
        url_text = ' '.join(list_text)

    else:
        url_text = t['text']

    print(url_text)

    return {'bank': t['bank'],
            'tweet_id': t['id'],
            'tweet_create_at': parser.parse(t['created_at']),
            'user_id': t['user']['id'],
            'user_since': parser.parse(t['user']['created_at']),
            'user_friends_count': t['user']['friends_count'],
            'user_followers_count': t['user']['followers_count'],
            'user_location': t['user']['location'],
            'truncated': t['truncated'],
            'tweet_text': t['text'],
            'url_text': url_text,
            'blob': json.dumps(t)}


class TwitterBanksSqLite(pw.Model):
    class Meta:
        database = pw.SqliteDatabase(DATA_STORAGE_DIR + 'twitterbanks.db')


class TwitterBanks(TwitterBanksSqLite):
    tweet_id = pw.CharField(unique=True, null=False, primary_key=True)
    tweet_create_at = pw.DateTimeField(index=True)
    user_id = pw.CharField()
    user_since = pw.DateTimeField()
    user_friends_count = pw.IntegerField()
    user_followers_count = pw.IntegerField()
    user_location = pw.CharField()
    bank = pw.CharField()
    truncated = pw.BooleanField()
    tweet_text = pw.TextField()
    url_text = pw.TextField()
    blob = pw.TextField()

    def create_or_ignore_table(self):
        if self.table_exists() == False:
            self.create_table()

    @classmethod
    def get_max_tweet_id(cls, bank):
        if cls.table_exists() and cls.select().where(cls.bank == bank).count() > 0:
            return int(cls.select(pw.fn.Max(cls.tweet_id)).where(cls.bank == bank).scalar())
        else:
            return None
