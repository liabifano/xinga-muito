import json
from logging import warning
from multiprocessing import Pool
from time import sleep

from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from toolz import interpose, valmap, merge_with

from xinga_muito import model
from xinga_muito.io import request_twitter
from xinga_muito.settings import BOOTSTRAP_ID, URL_QUERY, SLEEP_TIME_REQUESTS, ENGINE


def query_maker(key_words, count):
    return {'q': ' '.join(interpose('OR', key_words)),
            'since_at': 0,
            'count': count,
            'lang': 'pt'}


def get_max_id_api(query):
    response = request_twitter(URL_QUERY, 'GET', parameters=query)
    return json.loads(response.read())['search_metadata']['max_id']


def get_max_id_db(s, bank):
    r = s.query(func.max(model.TwitterBanks.id)).filter_by(bank=bank).scalar()
    return int(r) if r else None


def get_parse_save_tweets(session, bank, query, max_id_available_api):
    '''
    Get unparsed data, parse the data and save in a SQL database
    '''

    max_id_stored = get_max_id_db(session, bank)

    max_id_stored = max(max_id_stored, BOOTSTRAP_ID) if max_id_stored else BOOTSTRAP_ID

    max_id_to_consume = max_id_available_api

    print('')
    warning('Running: %s' % str(query['q']))
    print('')

    while max_id_to_consume > max_id_stored:
        sleep(SLEEP_TIME_REQUESTS)
        query['max_id'] = max_id_to_consume
        response = request_twitter(URL_QUERY, 'GET', parameters=query)

        tweets = json.loads(response.read())['statuses']
        tweets = [t for t in tweets if t['id'] > max_id_stored] # just in case
        tweets = [dict(item, bank=bank) for item in tweets]

        treated_tweets = [model.parse_one_twitter_output(t) for t in tweets]
        treated_tweets_db = [model.TwitterBanks(**t) for t in treated_tweets]
        session.add_all(treated_tweets_db)
        session.commit()

        try:
            max_id_to_consume = min([t['id'] for t in treated_tweets]) - 1
        except ValueError:
            break  # no more tweets to be consumed


def from_twitter(key_words):
    queries_max_id = valmap(lambda x: query_maker(x, 1), key_words)
    queries = valmap(lambda x: query_maker(x, 100), key_words)

    p = Pool(len(key_words))
    p.map(get_max_id_api, queries_max_id.values())
    max_ids = dict(zip(queries_max_id.keys(), p.map(get_max_id_api, queries_max_id.values())))

    requests_param = merge_with(lambda x: {'query': x[0], 'max_id_available_api': x[1]},
                                queries,
                                max_ids)

    engine = create_engine(ENGINE)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for bank in requests_param.keys():
        get_parse_save_tweets(session, bank, **requests_param[bank])

    session.close()
