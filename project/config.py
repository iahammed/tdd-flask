# project/config.py
import os

class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABSE_URI = os.environ.get('DATABASE_URL')

class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABSE_URI = os.environ.get('DATABASE_TEST_URL')
    
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABSE_URI = os.environ.get('DATABASE_URL')

