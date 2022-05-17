import os

class Config:
    '''
    General configuration parent class
    '''
    pass

    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTES_BASE_URL =' http://quotes.stormconsultancy.co.uk/popular.json'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}