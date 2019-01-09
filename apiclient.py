import requests
import json
from settings import URI, POST_URI, COLL_URI, set_token

# URI = constants.URI


def create_post(body, title):
    data = {"body": body,
            "title": title}

    try:
        p = requests.post(POST_URI, data=json.dumps(data),
                headers={"Content-Type":"application/json"})
    except Exception as e:
        print("create_post: Exception %s" % e)
        return e

    post = p.json()["data"]

    return post

def retrieve_post(id):
    try:
        p = requests.get(POST_URI + "/%s" % id,
            headers={"Content-Type":"application/json"})

    except Exception as e:
        print("retrieve_post: Exception %s" % e)
        return e

    post = p.json()["data"]

    return post

def update_post(id, token, body):
    data = {"token": token,
            "body": body}

    try:
        p = requests.post(POST_URI + "/%s" % id, data=json.dumps(data),
            headers={"Content-Type":"application/json"})

    except Exception as e:
        print("update_post: Exception %s" % e)
        return e

    post = p.json()["data"]

    return post

def delete_post(id, token):
    data = {"token": token}
    try:
        p = requests.delete(POST_URI + "/%s" % id, params=data)

    except Exception as e:
        print("delete_post: Exception %s" % e)
        return e

    post = p.raise_for_status()

    return post
    #Should return an error or something

def claim_post(id, token):
    data = [{"id": id,
            "token": token}]

    auth_token = set_token("b651ed4d-d5f0-4009-48f6-1c6d06f1f65e")

    try:
        p = requests.post(POST_URI + "/claim", data=json.dumps(data),
            headers={"Authorization": "Token %s" % auth_token,
                    "Content-Type": "application/json"})

    except Exception as e:
        print("claim_post: Exception %s" % e)
        return e

    post = p.json()["data"]

    return post
    # Should return a 200 in the post data to show it is claimed

def unpublish_post(id, token):
    data = {"token": token,
            "body": ""}

    try:
        p = requests.post(POST_URI + "/%s" % id, data=json.dumps(data),
            headers={"Content-Type":"application/json"})

    except Exception as e:
        print("update_post: Exception %s" % e)
        return e

    post = p.raise_for_status()

    return post
    # Should return a 410 with a message about post being unpublished


def create_collection(alias, title):
    data = {"alias": alias,
            "title": title}

    auth_token = set_token("b651ed4d-d5f0-4009-48f6-1c6d06f1f65e")

    try:
        c = requests.post(COLL_URI, data=json.dumps(data),
            headers={"Authorization": "Token %s" % auth_token,
                    "Content-Type": "application/json"})

    except Exception as e:
        print("create_collection: Exception %s" % e)
        return e

    collection = c.json()["data"]

    return collection


def retrieve_collection(alias):
    auth_token = set_token("b651ed4d-d5f0-4009-48f6-1c6d06f1f65e")

    try:
        c = requests.get(COLL_URI + "/%s" % alias,
            headers={"Authorization": "Token %s" % auth_token,
                    "Content-Type": "application/json"})

    except Exception as e:
        print("retrieve_collection: Exception %s" % e)
        return e

    collection = c.json()["data"]

    return collection

def retrieve_cpost(alias, slug):
    try:
        c = requests.get(COLL_URI + "/%s/posts/%s" % (alias, slug),
        headers={"Content-Type": "application/json"})

    except Exception as e:
        print("retrieve_cpost: Exception %s" % e)
        return e

    cpost = c.json()["data"]

    return cpost

def retrieve_cposts(alias):
    try:
        c = requests.get(COLL_URI + "/%s/posts" % alias)

    except Exception as e:
        print("retrieve_cposts: Exception %s" % e)
        return e

    cposts = c.json()["data"]

    return cposts

def delete_collection(alias):
    auth_token = set_token("b651ed4d-d5f0-4009-48f6-1c6d06f1f65e")

    try:
        c = requests.delete(COLL_URI + "/%s" % alias,
            headers={"Authorization": "Token %s" % auth_token,
                    "Content-Type": "application/json"})

    except Exception as e:
        print("retrieve_collection: Exception %s" % e)
        return e

    collection = c.json()["data"]

    return collection
    # Works if it returns an error that no json can be decoded
    # Perhaps write an if statement that if no json then success

def claim_cpost(alias, id, token):
    auth_token = set_token("b651ed4d-d5f0-4009-48f6-1c6d06f1f65e")

    data = [{"id": id,
            "token": token}]

    try:
        p = requests.post(COLL_URI + "/%s/collect" % alias, data=json.dumps(data),
            headers={"Authorization": "Token %s" % auth_token,
                    "Content-Type": "application/json"})

    except Exception as e:
        print("claim_cpost: Exception %s" % e)

    post = p.json()["data"]

    return post

def create_cpost(body, title, alias):
    auth_token = set_token("b651ed4d-d5f0-4009-48f6-1c6d06f1f65e")

    data = {"body": body,
            "title": title}

    try:
        p = requests.post(COLL_URI + "/%s/posts" % alias, data=json.dumps(data),
            headers={"Authorization": "Token %s" % auth_token,
                    "Content-Type": "application/json"})

    except Exception as e:
        print("retrieve_collection: Exception %s" % e)
        return e

    post = p.json()["data"]

    return post

def pin_post(alias, id, position):
    auth_token = set_token("b651ed4d-d5f0-4009-48f6-1c6d06f1f65e")

    data = [{"id": id,
            "position": position,}]

    try:
        p = requests.post(COLL_URI + "/%s/pin" % alias, data=json.dumps(data),
            headers={"Authorization": "Token %s" % auth_token,
                    "Content-Type": "application/json"})

    except Exception as e:
        print("pin_post: Exception %s" % e)
        return e

    post = p.json()["data"]

    return post

def unpin_post(alias, id):
    auth_token = set_token("b651ed4d-d5f0-4009-48f6-1c6d06f1f65e")

    data = [{"id": id}]

    try:
        p = requests.post(COLL_URI + "/%s/unpin" % alias, data=json.dumps(data),
            headers={"Authorization": "Token %s" % auth_token,
                    "Content-Type": "application/json"})

    except Exception as e:
        print("pin_post: Exception %s" % e)
        return e

    post = p.json()["data"]

    return post





# ---
# something.py
# ---
# from apiclient import authorize_user, create_post
#
# def get_creds():
#     """Ask the user for user and pass"""
#     creds_stuff.append('user')
#     creds_stuff.append('pass')
#     '''
#     ['user','pass']
#     '''
#     return creds_stuff
#
# def main():
#     cred_list = get_creds()
#     token = authorize_user(cred_list[0], cred_list[1],content_type='test/plain')
