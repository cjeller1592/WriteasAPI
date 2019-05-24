# Writeas API
An unofficial [Write.as](https://write.as) API client library for Python.

```
pip install writeasapi
```
### Version 0.1.8
- Updated class and module structure (cleaner and easier to read)
- More verbose exception handling using built in Write.as API responses
- Ability to now properly log off and delete posts/collections
- Access to Read.write.as API endpoint

If you have < 0.1.8, please update to this latest version. Otherwise you might run into issues.

```
pip install --upgrade writeasapi
```

_TODO:_
- ~~Include method for read.write.as endpoint~~
- ~~Proper exception handling~~
- Have the ability to retrieve posts within a collection that have certain tags (testing in tags.py)

## **Getting Started**

_Importing and Instanstiating:_
Each request to the API will be made through an instance of the client class. You can instantiate in two ways:

```
import writeas

c = writeas.client()

```
or...

```
from writeas import client

c = client()

# It is up to you really!
```

_Logging in and Setting Token:_
Make sure to login and set the token, otherwise certain authorized requests will not be possible.

```
from writeas import client

c = client()

c.login("username", "password")

# This prints out the user data which includes the access token
# We will store the token into the client instance for authenticated requests

c.setToken("00000000-0000-0000-0000-000000000000")

# Prints out the token and you are set to use the API!
```

_Logging Out:_
To log out, all you need is call the method.

```
c.logout()
"You are logged out!"

# The access token shouldn't work in a future request after logging out
```


## **Posts**
_Retrieving a Post:_
For finding a post, all you need is the post's id.

```
p = c.retrievePost('7qmni7cpg5sjks11')
print(p)

# This will return the post's data
```

_Creating an Annonymous Post:_
To create a post, all you need is a body. The title is optional!

```
p = c.createPost('This is a the body of the post.', 'This is a Title')
print p

# This will return the post's data when successful
# That data includes the post token which we'll need for doing cooling stuff with the post
```

_Creating a Collection Post:_
To create a collection post, all you need to add is the collection's alias to the above code.

```
p = c.createCPost('cjeller', 'This is a the body of the post.', 'This is a Title')
print(p)

# This will return the post's data 
```

_Updating a Post:_
All you need is the post's id and the parts of the post you want to edit. Since the updated part argument is set to kwargs in the code, be precise.

```
p = c.updatePost('7qmni7cpg5sjks11', body='I am updating this post's body!', title='Title Update!')
print(p)

# This will return the post's updated data when successful
```

_Deleting a Post:_
Since you are logged in, all you need is the post's id.

```
c.deletePost('7qmni7cpg5sjks11')
"Post deleted!"
```


## **Collections**

_Creating a collection:_ 
All you need is a collection alias and title.

```
collection = c.createCollection('collectionalias', 'My Cool Blog')
print collection

# This will return the collection's data
# Keep the collection's alias at hand: it will be a token for making requests with the collection
```

_Retrieving a Collection:_
All you need is the collection's alias.

```
coll = c.retrieveCollection('collectionalias')
pritnt(coll)

# This will return the collection's data
```

_Deleting a Collection:_
Since you are logged in, all you need is the collection's alias.

```
delete = c.deleteCollection('collectionalias')
"Collection deleted!"
```

_Retrieve a Collection Post:_
To retrieve a collection post, all you need is the collection's alias and the post's slug. Say we want to grab this post: https://write.as/matt/stepping-back

```
p = c.retrieveCPost('matt', 'stepping-back')
print(p)

# This will return the post's data 
```

_Retrieve a Collection's Posts:_
To get a collection's posts, all you need is the collection's alias. So if I wanted to grab all the posts from here: https://write.as/matt/

```
posts = c.retrieveCPosts('matt')
print(posts)

# This will return data from all the collection's posts
```
NOTE - This method only returns the first 10 posts of a collection. If you want to access more than the first 10 posts, use the optional pagination argument:

```
posts = c.retrieveCPosts('matt', 2)

# Returns >= 10 posts from that page
# If there are no posts on a selected page it will return an empty list
```

## **User**

_Retrieve User:_

```
me = c.retrieveUser()
print(me)

# Returns your user info 
```
_Retrieve User Posts:_

```
myPosts = c.retrievePosts()
print(myPosts)

# Returns your posts with this user account
```

_Retrieve User Collections:_

```
myCollections = c.retrieveCollections()
print(myCollections)

# Returns your collections
```

_Retrieve User Channels:_

```
myChannels = c.retrieveChannels()
print(myChannels)

# Returns the channels you send your posts to (Tumblr, Medium, etc)
```

## **Read.write.as**

[Read.write.as](https://read.write.as) is a way to read Write.as posts from writers who have their posts/blogs set for public display. Think of it as a feed for all kinds of writing.

_Retrieve Read.write.as Posts:_

```
rwaPosts = c.rwa()
print(rwaPosts)

# Returns 10 of the most recent Read.write.as posts
# Metadata is similar to retrieving a collection
```
The only argument available is skip. This specifies the number of posts to skip. Think of it as pagination:

```
rwaPosts = c.rwa(10)
print(rwaPosts)

# Returns 10 Read.write.as post, skipping the 10 most recent
```
