import base64, requests, json, sys

CONSUMER_KEY    = sys.argv[1]
CONSUMER_SECRET = sys.argv[2]

def get_bearer_token():
    concat = (CONSUMER_KEY + ':' + CONSUMER_SECRET).encode()
    b = base64.b64encode(concat).decode()
    (url,headers) = (
                        'https://api.twitter.com/oauth2/token',
                        {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "Basic %s" % b}
                    )

    token = requests.post(url, data={'grant_type': 'client_credentials'}, headers=headers)
    return json.loads(token.content)['access_token']


print(get_bearer_token())
