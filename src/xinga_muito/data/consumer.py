import json

from toolz import interpose, valmap, merge_with
from multiprocessing import Pool
from time import sleep, time
from logging import warning
from xinga_muito.settings import BOOTSTRAP_ID, URL_QUERY, HTTP_METHOD, SLEEP_TIME_REQUESTS
from xinga_muito.data import data_model
from xinga_muito.data.io import request_twitter


def query_maker(key_words, count):
    return {'q': ' '.join(interpose('OR', key_words)),
            'since_at': 0,
            'count': count,
            'lang': 'pt'}


def get_max_id_in_api(query):
    response = request_twitter(URL_QUERY, HTTP_METHOD, parameters=query)
    return json.loads(response.read())['search_metadata']['max_id']


def get_parse_save_tweets(db_conn, query, max_id_available_api):
    '''
    Get unparsed data, parse the data and save in a SQL database
    '''

    db_conn.create_or_ignore_table()
    max_id_stored = db_conn.get_max_tweet_id() or BOOTSTRAP_ID

    max_id_to_consume = max_id_available_api

    warning('Running: %s' % str(query['q']))

    while max_id_to_consume > max_id_stored:
        sleep(SLEEP_TIME_REQUESTS)
        query['max_id'] = max_id_to_consume
        response = request_twitter(URL_QUERY, HTTP_METHOD, parameters=query)

        tweets = json.loads(response.read())['statuses']
        tweets = map(lambda t: data_model.parse_one_twitter_output(t, query['q']), tweets)

        map(lambda t: db_conn.create_or_get(**t), tweets)

        try:
            max_id_to_consume = min(map(lambda t: t['tweet_id'], tweets))
        except ValueError:
            break # not more tweets to be consumed



def from_twitter(key_words):
    queries_max_id = valmap(lambda x: query_maker(x, 1), key_words)
    queries = valmap(lambda x: query_maker(x, 100), key_words)

    p = Pool(len(key_words))
    p.map(get_max_id_in_api, queries_max_id.values())
    max_ids = dict(zip(queries_max_id.keys(), p.map(get_max_id_in_api, queries_max_id.values())))

    requests_param = merge_with(lambda x: {'query': x[0], 'max_id_available_api': x[1]}, queries, max_ids)

    # TODO: fix this mess and also in data_model (ta uma macarronada)
    # TODO: make it deal with fails, use future
    get_parse_save_tweets(data_model.NubankTweets(), **requests_param['nubank'])
    get_parse_save_tweets(data_model.ItauTweets(), **requests_param['itau'])
    get_parse_save_tweets(data_model.BradescoTweets(), **requests_param['bradesco'])
    get_parse_save_tweets(data_model.DigioTweets(), **requests_param['digio'])
    get_parse_save_tweets(data_model.OriginalTweets(), **requests_param['original'])
    get_parse_save_tweets(data_model.BrasilTweets(), **requests_param['brasil'])
    get_parse_save_tweets(data_model.SantanderTweets(), **requests_param['santander'])
    get_parse_save_tweets(data_model.CaixaTweets(), **requests_param['caixa'])
