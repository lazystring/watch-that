class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments.
    JSON_ADD_STATUS = False

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

class TestingConfig(Config):
    """
    Configurations for testing.
    """

    Testing = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    PRESERVE_CONTEXT_ON_EXCEPTION = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
