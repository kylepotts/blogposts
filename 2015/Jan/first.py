class first_post(object):
    def __init__(self):
        self.numPosts = 1


    def __repr__(self):
        return "I have made %d posts" %(self.numPosts)


post = first_post()
print(post)
