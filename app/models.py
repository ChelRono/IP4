from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




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

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))


    def __repr__(self):
        return f'User {self.username}'

    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'