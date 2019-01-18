# Writeas.py
An API client library for [Write.as](https://write.as) written for Python.

## **Authentication**

```
c = NewClient()

c.login("username", "password")

# This prints out the user data which includes the access token
# We will store the token into the client instance for authenticated requests

c.setToken("00000000-0000-0000-0000-000000000000")

# Prints out the token and you are set to use the API!
```


## **Posts**

_Creating a post:_

```
p = c.create_post("This is a the body of the post.", "This is a Title")

# This will return the post's data when successful
# That data includes the post token which we'll need for doing cooling stuff with the post
```

_Updating a Post:_
All you need is the post's id, the post's token, and the part of the post you want to edit.

```
update = c.updatePost('7qmni7cpg5sjks11', '123456789abcdefgthisisfakeposttoken', 'I am updating this post's body!')

# This will return the post's data when successful
```

_Deleting a Post:_
Since you are logged in, all you need is the post's id.

```
delete = c.delete_post('7qmni7cpg5sjks11')

# This will return a 'None', meaning that it worked
```


_Retrieving a Post:_
For finding a post, all you need is the post's id.

```
post = c.find_post('7qmni7cpg5sjks11')

# This will return the post's data
```

_Claiming a Post_:
If you create an anonymous post but want to claim it, all you need is the post's id and token

```
post = c.claimPost('7qmni7cpg5sjks11', ''123456789abcdefgthisisfakeposttoken')

# This will return the post's data
```


## **Collections**

_Creating a collection:_ 
All you need is a collection alias and title.

```
collection = c.createCollection('collectionalias', 'My Cool Blog')

# This will return the collection's data
# Keep the collection's alias at hand: it will serve as the token for doing cool stuff with our collection
```

_Retrieving a Collection:_
All you need is the collection's alias.

```
collection = c.retrieveCollection('collectionalias')

# This will return the collection's data
```

_Deleting a Collection:_
All you need is the collection's alias.

```
delete = c.deleteCollection('collectionalias')

# This will return a 'None', meaning it was successfully deleted
```

_Retrieve a Collection Post:_
To retrieve a collection post, all you need is the slug of the post and the collection's alias. Say we want to grab this post: https://write.as/matt/stepping-back

```
post = c.retrieveCPost('why-i-still-love-computers', 'natedickson')

# This will return the post's data 
```

_Retrieve a Collection's Posts:_
To get a collection's posts, all you need is the collection's alias. So if I wanted to grab all the posts from here: https://write.as/matt/

```
posts = c.retrieveCPosts('matt')

# This will return data from all the collection's posts
```


