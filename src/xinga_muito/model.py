import json
import requests
from bs4 import BeautifulSoup, element
from dateutil import parser
from w3lib.html import remove_tags

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Boolean, Text, schema
from sqlalchemy.ext.declarative import declarative_base


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

    return {'bank': str(t['bank']),
            'id': t['id'],
            'created_at': parser.parse(t['created_at']),
            'user_id': t['user']['id'],
            'user_since': parser.parse(t['user']['created_at']),
            'user_friends_count': t['user']['friends_count'],
            'user_followers_count': t['user']['followers_count'],
            'user_location': t['user']['location'],
            'truncated': t['truncated'],
            'tweet_text': t['text'],
            'url_text': url_text,
            'blob': json.dumps(t)}


Base = declarative_base()


class TwitterBanks(Base):
    __tablename__ = 'tweets'
    __table_args__ = (schema.UniqueConstraint('id', 'bank', name='id_bank'),)

    id = Column(String, primary_key=True, nullable=False, autoincrement=True)
    bank = Column(String, primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(String, nullable=False)
    user_since = Column(DateTime, nullable=False)
    user_friends_count = Column(Integer, nullable=True)
    user_followers_count = Column(Integer, nullable=True)
    user_location = Column(String, nullable=True)
    truncated = Column(Boolean, nullable=True)
    tweet_text = Column(Text, nullable=True)
    url_text = Column(Text, nullable=True)
    blob = Column(Text(), nullable=True)

    # @classmethod
    # def get_max_tweet_id(cls, bank):
    #     if cls.table_exists() and cls.select().where(cls.bank == bank).count() > 0:
    #         return int(cls.select(pw.fn.Max(cls.tweet_id)).where(cls.bank == bank).scalar())
    #     else:
    #         return None

    def __repr__(self):
        return
