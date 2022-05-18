import os

class Config:
    '''
    General configuration parent class
    '''
    pass

   
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTES_BASE_URL =' http://quotes.stormconsultancy.co.uk/popular.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://valarie:1033927@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    

class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://valarie:1033927@localhost/blog'
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://valarie:1033927@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}