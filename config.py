import os

basedir = os.path.abspath(os.path.dirname(__name__))

def getDataBaseUri(env = None):
    if env is not None:
        return os.environ.get('{}.DATABASE_URI'.format(env.upper())) or 'sqlite:///' + os.path.join(basedir, '{}.data.sqlite'.format(env.lower()))
    return os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

class Config:
    GLOBAL_SECRET = 'global secret code' or os.environ.get('GLOBAL_SECRET')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    ADMIN = os.environ.get('ADMIN')
    MAIL_SUBJECT_PREFIX = '[subject]-'
    MAIL_SENDER = 'Joe.C.Zhou<joe_c_zhou@163.com>'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = getDataBaseUri()

class DevConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = getDataBaseUri('dev')

class TestConfig(Config):
    TEST = True
    SQLALCHEMY_DATABASE_URI = getDataBaseUri('test')

config = {
    "development": DevConfig,
    "production": ProductionConfig,
    "test": TestConfig,
    "default": DevConfig
}