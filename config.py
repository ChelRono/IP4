import os

class Config:

    '''
    class config
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    QUOTES_BASE_URL =' http://quotes.stormconsultancy.co.uk/popular.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://valarie:1033927@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
class TestConfig(Config):
    '''
    test configurations
    '''
    pass
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    pass
config_options = {
'development':DevConfig,
'test':TestConfig,
'production':ProdConfig
}