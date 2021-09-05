class Config(object):
    SECRET_KEY = b"\xd2\xeb\x82K+p\xc5\xec9\xf9\x9af<\xd0\xb3\x10\x0f\x87=\xab\xb3M;\xa6"

    SESSION_COOKIE_PATH = "/"
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

    DB_NAME = "production-db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///database/{DB_NAME}.db"

    SESSION_COOKIE_SECURE = True


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

    DB_NAME = "development-db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///database/{DB_NAME}.db"

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True

    DB_NAME = "development-db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///database/{DB_NAME}.db"

    SESSION_COOKIE_SECURE = False
