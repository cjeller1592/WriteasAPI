import requests
import json
from settings import URI, POST_URI, COLL_URI, ME_URI,

class NewClient(object):
    def __init__(self):
        self.token = ""

    def login(self, user, password):
    # This is how you will authenticate your Write.as account and retreive an access token for future requests

        data = {"alias": user, "pass": password }

        try:
            r = requests.post(URI, data=json.dumps(data),
                            headers={"Content-Type":"application/json"})
        except Exception as e:
            print("login: Execption: %s" % e)
            return e

    # Once the request is successfully sent, we will grab the user data
    # Here will be the token we need for authorized requests
        user = r.json()['data']

        return user

    def set_token(self, auth_token):

    # The token will look like this: "00000000-0000-0000-0000-000000000000"
        self.token = auth_token
        return self.token

    def logout(self, auth_token):
        try:
            r = requests.delete("https://write.as/api/auth/me",
                headers="Authorization: Token %s" % auth_token)

        except Exception as e:
            print("logout: Exception: %s" % e)
            return e

        user = r.json()["data"]


    def retrieve_user(self):

        try:
            u = requests.get(ME_URI,
            headers={"Authorization":"Token %s" % self.token,
                "Content-Type":"application/json"})

        except Exception as e:
            print("retrieve_user: Exception %s" % e)
            return e

        user = u.json()["data"]

        return user

    def retrieve_uposts(self):

        try:
            p = requests.get(ME_URI + "/posts",
            headers={"Authorization":"Token %s" % self.token,
                "Content-Type":"application/json"})

        except Exception as e:
            print("retrieve_uposts: Exception %s" % e)
            return e

        uposts = p.json()["data"]

        return uposts

    def retrieve_ucollections(self):

        try:
            c = requests.get(ME_URI + "/collections",
            headers={"Authorization":"Token %s" % self.token,
                "Content-Type":"application/json"})

        except Exception as e:
            print("retrieve_ucollections: Exception %s" % e)
            return e

        ucollections = c.json()["data"]

        return ucollections

    def retrieve_uchannels(self):
        try:
            c = requests.get(ME_URI + "/channels",
            headers={"Authorization":"Token %s" % self.token,
                "Content-Type":"application/json"})

        except Exception as e:
            print("retrieve_ucollections: Exception %s" % e)
            return e

        uchannels = c.json()["data"]

        return uchannels


    def create_post(self, body, title):
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

    def retrieve_post(self, id):

        try:
            p = requests.get(POST_URI + "/%s" % id,
                headers={"Content-Type":"application/json"})

        except Exception as e:
            print("retrieve_post: Exception %s" % e)
            return e

        post = p.json()["data"]

        return post

    def update_post(self, id, token, body):
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

    def delete_post(self, id):

        try:
            p = requests.delete(POST_URI + "/%s" % id,
            headers={"Authorization": "Token %s" % self.token,
                    "Content-Type": "application/json"})

        except Exception as e:
            print("delete_post: Exception %s" % e)
            return e

        post = p.raise_for_status()

        return post
        #Should return an error or something

    def claim_post(self, id, token):
        data = [{"id": id,
                "token": token}]

        try:
            p = requests.post(POST_URI + "/claim", data=json.dumps(data),
                headers={"Authorization": "Token %s" % self.token,
                        "Content-Type": "application/json"})

        except Exception as e:
            print("claim_post: Exception %s" % e)
            return e

        post = p.json()["data"]

        return post
        # Should return a 200 in the post data to show it is claimed


    def unpublish_post(self, id, token):
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


    def create_collection(self, alias, title):

        data = {"alias": alias,
                "title": title}

        try:
            c = requests.post(COLL_URI, data=json.dumps(data),
                headers={"Authorization": "Token %s" % self.token,
                        "Content-Type": "application/json"})

        except Exception as e:
            print("create_collection: Exception %s" % e)
            return e

        collection = c.json()["data"]

        return collection


    def retrieve_collection(self, alias):

        try:
            c = requests.get(COLL_URI + "/%s" % alias,
                headers={"Authorization": "Token %s" % self.token,
                        "Content-Type": "application/json"})

        except Exception as e:
            print("retrieve_collection: Exception %s" % e)
            return e

        collection = c.json()["data"]

        return collection

    def retrieve_cpost(self, alias, slug):

        try:
            c = requests.get(COLL_URI + "/%s/posts/%s" % (alias, slug),
            headers={"Content-Type": "application/json"})

        except Exception as e:
            print("retrieve_cpost: Exception %s" % e)
            return e

        cpost = c.json()["data"]

        return cpost

    def retrieve_cposts(self, alias):

        try:
            c = requests.get(COLL_URI + "/%s/posts" % alias)

        except Exception as e:
            print("retrieve_cposts: Exception %s" % e)
            return e

        cposts = c.json()["data"]

        return cposts

    def delete_collection(self, alias):

        try:
            c = requests.delete(COLL_URI + "/%s" % alias,
                headers={"Authorization": "Token %s" % self.token,
                        "Content-Type": "application/json"})

        except Exception as e:
            print("retrieve_collection: Exception %s" % e)
            return e

        collection = c.json()["data"]

        return collection
        # Works if it returns an error that no json can be decoded
        # Perhaps write an if statement that if no json then success

    def claim_cpost(self, alias, id, token):

        data = [{"id": id,
                "token": token}]

        try:
            p = requests.post(COLL_URI + "/%s/collect" % alias, data=json.dumps(data),
                headers={"Authorization": "Token %s" % self.token,
                        "Content-Type": "application/json"})

        except Exception as e:
            print("claim_cpost: Exception %s" % e)

        post = p.json()["data"]

        return post

    def create_cpost(self, body, title, alias):

        data = {"body": body,
                "title": title}

        try:
            p = requests.post(COLL_URI + "/%s/posts" % alias, data=json.dumps(data),
                headers={"Authorization": "Token %s" % self.token,
                        "Content-Type": "application/json"})

        except Exception as e:
            print("retrieve_collection: Exception %s" % e)
            return e

        post = p.json()["data"]

        return post

    def pin_post(self, alias, id, position):

        data = [{"id": id,
                "position": position,}]

        try:
            p = requests.post(COLL_URI + "/%s/pin" % alias, data=json.dumps(data),
                headers={"Authorization": "Token %s" % self.token,
                        "Content-Type": "application/json"})

        except Exception as e:
            print("pin_post: Exception %s" % e)
            return e

        post = p.json()["data"]

        return post

    def unpin_post(self, alias, id):

        data = [{"id": id}]

        try:
            p = requests.post(COLL_URI + "/%s/unpin" % alias, data=json.dumps(data),
                headers={"Authorization": "Token %s" % self.token,
                        "Content-Type": "application/json"})

        except Exception as e:
            print("pin_post: Exception %s" % e)
            return e

        post = p.json()["data"]

        return post



