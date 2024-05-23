import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class Development(object):
  DEBUG = True
  TESTING = False
  SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
  SECRET_KEY = os.getenv('SECRET_KEY')

class Production(object):
  DEBUG = False
  TESTING = False
  SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
  SECRET_KEY = os.getenv('SECRET_KEY')

app_config = { 'development': Development, 'production': Production }
