class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLE_URL='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    TOP_HEADLINES_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_KEY = '12ac3b30fdfe4c479c98a7b8ccf3968b'



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


config_options = {
'development':DevConfig,
'production':ProdConfig
}
