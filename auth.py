import requests
import json

from settings import URI


def login(user, password):
# This is how you will authenticate your Write.as account and retreive an access token for future requests

# 'Data' consists of your Write.as username and password
# FOR TESTING PURPOSES ONLY...MAKE SURE TO PROTECT THIS ONCE DEPLOYED
    data = {"alias": user, "pass": password }

    try:
        r = requests.post(URI, data=json.dumps(data),
                        headers={"Content-Type":"application/json"})
    except Exception as e:
        print("log_in: Execption: %s" % e)
        return e

# Once the request is successfully sent, we will grab the user data
# Here will be the token we need for authorized requests
    user = r.json()['data']

    return user

def set_token(auth_token):

# The token will look like this: "00000000-0000-0000-0000-000000000000"
    token = auth_token
    return token
