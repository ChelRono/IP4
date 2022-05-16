class Config:
    '''
    General configuration parent class
    '''
    pass

    QUOTE_URL='  http://quotes.stormconsultancy.co.uk/popular.json'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True