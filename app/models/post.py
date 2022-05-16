class Post:

    all_posts = []

    def __init__(self,author,quote):
        
        self.author = author
        self.quote = quote


    def save_post(self):
        Post.all_posts.append(self)


    @classmethod
    def clear_reviews(cls):
        Post.all_posts.clear()