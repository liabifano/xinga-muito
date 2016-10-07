import oauth2 as oauth
import urllib2 as urllib

from xinga_muito.settings import OAUTH_CONSUMER, OAUTH_TOKEN, SIGNATURE_METHOD, HTTP_HANDLER, HTTPS_HANDLER


def request_twitter(url, method, parameters):
    '''
    Open connection with twitter API, get data and close the connection
    '''
    req = oauth.Request.from_consumer_and_token(consumer=OAUTH_CONSUMER,
                                                token=OAUTH_TOKEN,
                                                http_method=method,
                                                http_url=url,
                                                parameters=parameters)

    req.sign_request(SIGNATURE_METHOD, OAUTH_CONSUMER, OAUTH_TOKEN)

    url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(HTTP_HANDLER)
    opener.add_handler(HTTPS_HANDLER)

    response = opener.open(url)

    return response