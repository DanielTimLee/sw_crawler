import os

# db
DATABASE_HOST = 'localhost:3306'
DATABASE_USERNAME = 'root'
DATABASE_PASSWORD = 'daniel'
DEFAULT_DATABASE = 'sw_crawler'

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}/{3}".format(DATABASE_USERNAME,
                                                                   DATABASE_PASSWORD,
                                                                   DATABASE_HOST,
                                                                   DEFAULT_DATABASE)

SECRET_KEY = os.environ['SECRET_KEY']
CRAWLER_EMAIL = os.environ['CRAWLER_EMAIL']
CRAWLER_PWD = os.environ['CRAWLER_PWD']
TARGET = os.environ['TARGET']

SQLALCHEMY_TRACK_MODIFICATIONS = True

TEMPLATES_AUTO_RELOAD = True
