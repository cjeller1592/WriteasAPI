# Want to instanciate the client
import requests
import json
from uri import URI

from user import user
from posts import post
from collection import collection
from rwa import readwa

class client():
    def __init__(self):
        self.token = ""
        self.u = user()
        self.p = post()
        self.c = collection()
        self.r = readwa()
# AUTH
    def login(self, username, password):
        user = self.u.auth(username, password)
#        self.token = user['access_token']
# Doing this might make any error handling trickier
# Because if the fxn fails then getting the token will fail and not give me any useful info
        return user

    def setToken(self, token):
        self.token = token
        return 'The auth token is set!'

    def checkToken(self):
        return self.token

    def logout(self):
        user = self.u.authout(self.token)
        return user

# USER
    def retrievePosts(self):
        posts = self.u.getPosts(self.token)
        return posts

    def retrieveCollections(self):
        collections = self.u.getCollections(self.token)
        return collections

    def retrieveChannels(self):
        channels = self.u.getChannels(self.token)
        return channels

# POST
    def retrievePost(self, id):
        post = self.p.get(id)
        return post

    def createPost(self, body, title=None, **kwargs):
        post = self.p.post(self.token, body, title, **kwargs)
        return post

    def updatePost(self, id, **kwargs):
        post = self.p.update(self.token, id, **kwargs)
        return post

    def deletePost(self, id):
        post = self.p.delete(self.token, id)
        return post

    def claimPost(self, id, ptoken):
        post = self.p.claim(self.token, id, ptoken)
        return post

# COLLECTION
    def retrieveCollection(self, alias):
        collection = self.c.get(alias)
        return collection

    def createCollection(self, alias, title):
        collection = self.c.post(self.token, alias, title)
        return collection

    def deleteCollection(self, alias):
        collection = self.c.delete(self.token, alias)
        return collection

    def retrieveCPost(self, alias, slug):
        cpost = self.c.getCP(alias, slug)
        return cpost

    def retrieveCPosts(self, alias):
        cposts = self.c.getCPs(alias)
        return cposts

    def createCPost(self, alias, body, title=None, **kwargs):
        cpost = self.c.createCP(self.token, alias, body, title, **kwargs)
        return cpost

    def claimCPost(self, alias, id):
        cpost = self.c.claimCP(self.token, alias, id)
        return cpost

    def pinPost(self, alias, id, position=1):
        post = self.c.pin(self.token, alias, id, position)
        return post

    def upinPost(self, alias, id):
        post = self.c.unpin(self.token, alias, id)

# READ WRITE.as
    def rwa(self, skip=0):
        posts = self.r.get(skip)
        return posts
