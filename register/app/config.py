class Config(object):
    """Base config class."""
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/imaw'
