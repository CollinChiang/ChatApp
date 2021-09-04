class Config(object):
    SECRET_KEY = b"\xd2\xeb\x82K+p\xc5\xec9\xf9\x9af<\xd0\xb3\x10\x0f\x87=\xab\xb3M;\xa6"

    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

    DB_NAME = "production-db"
    DB_USERNAME = ""
    DB_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI = None  # TODO create production database

    SESSION_COOKIE_SECURE = True


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

    DB_NAME = "development-db"
    DB_USERNAME = ""
    DB_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI = None  # TODO create development database

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True

    DB_NAME = "development-db"
    DB_USERNAME = ""
    DB_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI = None  # TODO create testing database

    SESSION_COOKIE_SECURE = False
