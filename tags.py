import writeas


def searchTags(collection, tag):
    c = writeas.NewClient()

    # Choose the collection
    cPosts = c.retrieveCPosts(collection)

    # Grab the collection posts
    posts = cPosts['posts']

    # Creating the list to store the matching tagged posts
    list = []

    # Embedded for loop: grab the tags for each posts
    # For each tag, compare to searched tag and store matches in lists
    for post in posts:
        ptags = post['tags']
        for ptag in ptags:
            if ptag == tag:
                list.append(post)

    # Return list that can be queried: ex. list[0]['title']
    return list
