# Writeas API
An unofficial [Write.as](https://write.as) API client library for Python.

```
pip install writeasapi
```
### Version 0.1.7
- Pagination for retrieving a collection's posts
- Access to [Read.write.as](https://read.write.as) API endpoint
- Adding title now optional for creating an annonymous or collection post

If need be, please update to this latest version

```
pip install --upgrade writeasapi
```

_TODO:_
- ~~Include method for read.write.as endpoint~~
- Proper exception handling
- Have the ability to retrieve posts within a collection that have certain tags (testing in tags.py)

## **Getting Started**

_Importing and Instanstiating:_
Each request to the API will be made through an instance of the NewClient class. You can instantiate in two ways:

```
import writeas

c = writeas.NewClient()

```
or...

```
from writeas import NewClient

c = NewClient()

# It is up to you really! This way may also be best for saving memory in a project that you aren't simply running locally
```


_Logging in and Setting Token:_
Make sure to login and set the token, otherwise certain authorized requests will not be possible.

```
from writeas import NewClient

c = NewClient()

c.login("username", "password")

# This prints out the user data which includes the access token
# We will store the token into the client instance for authenticated requests

c.setToken("00000000-0000-0000-0000-000000000000")

# Prints out the token and you are set to use the API!
```

_Logging Out:_
To log out, all you need is to put the access token in as an argument

```
c.logout("00000000-0000-0000-0000-000000000000")

# Returns a 204 status code
# The access token shouldn't work in a future request after logging out
```

## **Posts**

_Creating an annonymous post:_
To create a post, all you need is a body. The title is optional!

```
p = c.createPost('This is a the body of the post.', 'This is a Title')
print p

# This will return the post's data when successful
# That data includes the post token which we'll need for doing cooling stuff with the post
```
_Creating a collection post:_
To create a collection post, all you need to add is the collection's alias to the above code.
```
post = c.createCPost('cjeller', 'This is a the body of the post.', 'This is a Title')
print post

# This will return the post's data 
```


_Updating a Post:_
All you need is the post's id and the parts of the post you want to edit. Since the updated part argument is set to kwargs in the code, be precise.

```
update = c.updatePost('7qmni7cpg5sjks11', body='I am updating this post's body!', title='Title Update!')
print update

# This will return the post's updated data when successful
```

_Deleting a Post:_
Since you are logged in, all you need is the post's id.

```
delete = c.deletePost('7qmni7cpg5sjks11')
print delete

# This will return a 'None', meaning that it worked
```


_Retrieving a Post:_
For finding a post, all you need is the post's id.

```
post = c.retrievePost('7qmni7cpg5sjks11')
print post

# This will return the post's data
```

_Claiming a Post_:
If you create an anonymous post but want to claim it, all you need is the post's id and token

```
post = c.claimPost('7qmni7cpg5sjks11', '123456789abcdefgthisisfakeposttoken')
print post

# This will return the post's data
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
collection = c.retrieveCollection('collectionalias')
pritnt collection

# This will return the collection's data
```

_Deleting a Collection:_
All you need is the collection's alias.

```
delete = c.deleteCollection('collectionalias')
print delete

# This will return a 'None', meaning it was successfully deleted
```

_Retrieve a Collection Post:_
To retrieve a collection post, all you need is the collection's alias and the post's slug. Say we want to grab this post: https://write.as/matt/stepping-back

```
post = c.retrieveCPost('matt', 'stepping-back')
print post

# This will return the post's data 
```

_Retrieve a Collection's Posts:_
To get a collection's posts, all you need is the collection's alias. So if I wanted to grab all the posts from here: https://write.as/matt/

```
posts = c.retrieveCPosts('matt')
print posts

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
print me

# Returns your user info 
```
_Retrieve User Posts:_

```
myPosts = c.retrievePosts()
print myPosts

# Returns your posts with this user account
```

_Retrieve User Collections:_

```
myCollections = c.retrieveCollections()
print myCollections

# Returns your collections
```

_Retrieve User Channels:_

```
myChannels = c.retrieveChannels()
print myChannels

# Returns the channels you send your posts to (Tumblr, Medium, etc)
```

## **Read.write.as**

[Read.write.as](https://read.write.as) is a way to read Write.as posts from writers who have their blogs set for public display. Think of it as a feed of interesting writing.

_Retrieve Read.write.as Posts:_

```
rwaPosts = c.rwa()
print rwaPosts

# Returns 10 of the most recent Read.write.as posts
# Metadata is similar to retrieving a collection
```
The only argument available is skip. This is specifies the number of posts to skip, for implementing pagination:

```
rwaPosts = c.rwa(2)
print rwaPosts

# Returns 10 Read.write.as post, skipping the 2 most recent
```
