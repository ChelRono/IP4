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

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}