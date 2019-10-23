import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    SECRET_KEY = "secret key"
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    SECRET_KEY = "secret key"
    DEBUG = True
    #UPLOAD_FOLDER = '/home/leons/data-platform/data-upload/app/tests/temp_data'
    UPLOAD_FOLDER = '/flask-app'
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    ALLOWED_EXTENSIONS = set(['csv', 'txt'])
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    # PRESERVE_CONTEXT_ON_EXCEPTION = False
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
