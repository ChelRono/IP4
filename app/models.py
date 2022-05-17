from . import db




class Quotes:
    '''
    Quote class to define Movie Objects
    '''

    def __init__(self,author,quote):
        self.author= author
        self.quote = quote

class Post:

    all_posts = []

    def __init__(self,author,quote):
        
        self.author = author
        self.quote = quote


    def save_post(self):
        Post.all_posts.append(self)


    @classmethod
    def clear_post(cls):
        Post.all_posts.clear()

    @classmethod
    def get_post(cls,id):

        response = []

        for post in cls.all_posts:
            if post.quote_id == id:
                response.append(post)

        return response

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'