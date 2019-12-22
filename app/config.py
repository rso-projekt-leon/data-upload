import os


class BaseConfig:
    """Base configuration"""

    TESTING = False
    SECRET_KEY = "my_precious"
    ALLOWED_EXTENSIONS = ('csv')
    UPLOAD_FOLDER = '/home'


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DATA_CATALOG_URL = 'http://data-catalog:5000'


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    UPLOAD_FOLDER = '/home/app/app'
    DATA_CATALOG_URL = os.environ.get("DATA_CATALOG_URL")

