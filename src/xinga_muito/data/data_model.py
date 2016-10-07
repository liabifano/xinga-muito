import json
import peewee as pw
from dateutil import parser

from xinga_muito.settings import DATA_STORAGE_DIR


def parse_one_twitter_output(t, key_words):
    return {'key_words': key_words,
            'tweet_id': t['id'],
            'tweet_create_at': parser.parse(t['created_at']),
            'user_id': t['user']['id'],
            'user_since': parser.parse(t['user']['created_at']),
            'user_friends_count': t['user']['friends_count'],
            'user_followers_count': t['user']['followers_count'],
            'user_location': t['user']['location'],
            'tweet_text': t['text'],
            'blob': json.dumps(t)}


# TODO: figure out a better way to do it, it's a mess
class NubankSqLite(pw.Model):
    class Meta:
        database = pw.SqliteDatabase(DATA_STORAGE_DIR + 'nubank.db')


class NubankTweets(NubankSqLite):
    tweet_id = pw.CharField(unique=True, null=False, primary_key=True)
    tweet_create_at = pw.DateTimeField(index=True)
    user_id = pw.CharField()
    user_since = pw.DateTimeField()
    user_friends_count = pw.IntegerField()
    user_followers_count = pw.IntegerField()
    user_location = pw.CharField()
    tweet_text = pw.TextField()
    key_words = pw.TextField()
    blob = pw.TextField()

    def create_or_ignore_table(self):
        if self.table_exists() == False:
            self.create_table()

    @classmethod
    def get_max_tweet_id(cls):
        if cls.table_exists() and cls.select().count() > 0:
            return int(cls.select(pw.fn.Max(cls.tweet_id)).scalar())
        else:
            return None


class ItauSqLite(pw.Model):
    class Meta:
        database = pw.SqliteDatabase(DATA_STORAGE_DIR + 'itau.db')


class ItauTweets(ItauSqLite):
    tweet_id = pw.CharField(unique=True, null=False, primary_key=True)
    tweet_create_at = pw.DateTimeField(index=True)
    user_id = pw.CharField()
    user_since = pw.DateTimeField()
    user_friends_count = pw.IntegerField()
    user_followers_count = pw.IntegerField()
    user_location = pw.CharField()
    tweet_text = pw.TextField()
    key_words = pw.TextField()
    blob = pw.TextField()

    def create_or_ignore_table(self):
        if self.table_exists() == False:
            self.create_table()

    @classmethod
    def get_max_tweet_id(cls):
        if cls.table_exists() and cls.select().count() > 0:
            return int(cls.select(pw.fn.Max(cls.tweet_id)).scalar())
        else:
            return None


class BradescoSqLite(pw.Model):
    class Meta:
        database = pw.SqliteDatabase(DATA_STORAGE_DIR + 'bradesco.db')


class BradescoTweets(BradescoSqLite):
    tweet_id = pw.CharField(unique=True, null=False, primary_key=True)
    tweet_create_at = pw.DateTimeField(index=True)
    user_id = pw.CharField()
    user_since = pw.DateTimeField()
    user_friends_count = pw.IntegerField()
    user_followers_count = pw.IntegerField()
    user_location = pw.CharField()
    tweet_text = pw.TextField()
    key_words = pw.TextField()
    blob = pw.TextField()

    def create_or_ignore_table(self):
        if self.table_exists() == False:
            self.create_table()

    @classmethod
    def get_max_tweet_id(cls):
        if cls.table_exists() and cls.select().count() > 0:
            return int(cls.select(pw.fn.Max(cls.tweet_id)).scalar())
        else:
            return None


class DigioSqLite(pw.Model):
    class Meta:
        database = pw.SqliteDatabase(DATA_STORAGE_DIR + 'digio.db')


class DigioTweets(DigioSqLite):
    tweet_id = pw.CharField(unique=True, null=False, primary_key=True)
    tweet_create_at = pw.DateTimeField(index=True)
    user_id = pw.CharField()
    user_since = pw.DateTimeField()
    user_friends_count = pw.IntegerField()
    user_followers_count = pw.IntegerField()
    user_location = pw.CharField()
    tweet_text = pw.TextField()
    key_words = pw.TextField()
    blob = pw.TextField()

    def create_or_ignore_table(self):
        if self.table_exists() == False:
            self.create_table()

    @classmethod
    def get_max_tweet_id(cls):
        if cls.table_exists() and cls.select().count() > 0:
            return int(cls.select(pw.fn.Max(cls.tweet_id)).scalar())
        else:
            return None


class OriginalSqLite(pw.Model):
    class Meta:
        database = pw.SqliteDatabase(DATA_STORAGE_DIR + 'original.db')


class OriginalTweets(OriginalSqLite):
    tweet_id = pw.CharField(unique=True, null=False, primary_key=True)
    tweet_create_at = pw.DateTimeField(index=True)
    user_id = pw.CharField()
    user_since = pw.DateTimeField()
    user_friends_count = pw.IntegerField()
    user_followers_count = pw.IntegerField()
    user_location = pw.CharField()
    tweet_text = pw.TextField()
    key_words = pw.TextField()
    blob = pw.TextField()

    def create_or_ignore_table(self):
        if self.table_exists() == False:
            self.create_table()

    @classmethod
    def get_max_tweet_id(cls):
        if cls.table_exists() and cls.select().count() > 0:
            return int(cls.select(pw.fn.Max(cls.tweet_id)).scalar())
        else:
            return None


class BrasilSqLite(pw.Model):
    class Meta:
        database = pw.SqliteDatabase(DATA_STORAGE_DIR + 'brasil.db')


class BrasilTweets(BrasilSqLite):
    tweet_id = pw.CharField(unique=True, null=False, primary_key=True)
    tweet_create_at = pw.DateTimeField(index=True)
    user_id = pw.CharField()
    user_since = pw.DateTimeField()
    user_friends_count = pw.IntegerField()
    user_followers_count = pw.IntegerField()
    user_location = pw.CharField()
    tweet_text = pw.TextField()
    key_words = pw.TextField()
    blob = pw.TextField()

    def create_or_ignore_table(self):
        if self.table_exists() == False:
            self.create_table()

    @classmethod
    def get_max_tweet_id(cls):
        if cls.table_exists() and cls.select().count() > 0:
            return int(cls.select(pw.fn.Max(cls.tweet_id)).scalar())
        else:
            return None


class CaixaSqLite(pw.Model):
    class Meta:
        database = pw.SqliteDatabase(DATA_STORAGE_DIR + 'caixa.db')


class CaixaTweets(CaixaSqLite):
    tweet_id = pw.CharField(unique=True, null=False, primary_key=True)
    tweet_create_at = pw.DateTimeField(index=True)
    user_id = pw.CharField()
    user_since = pw.DateTimeField()
    user_friends_count = pw.IntegerField()
    user_followers_count = pw.IntegerField()
    user_location = pw.CharField()
    tweet_text = pw.TextField()
    key_words = pw.TextField()
    blob = pw.TextField()

    def create_or_ignore_table(self):
        if self.table_exists() == False:
            self.create_table()

    @classmethod
    def get_max_tweet_id(cls):
        if cls.table_exists() and cls.select().count() > 0:
            return int(cls.select(pw.fn.Max(cls.tweet_id)).scalar())
        else:
            return None
