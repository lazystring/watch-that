class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments.

class DevelopmentConfig(Config):
    """
    Configurations for development.
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Configurations for production.
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
