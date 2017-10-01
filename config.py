class Config(object):
    pass


class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):

    DEBUG = False


APP_CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
