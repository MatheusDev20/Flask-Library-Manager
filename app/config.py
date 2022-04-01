import os

class BaseConfiguration:
    TESTING = False
    SOME_RANDOM_TOKEN = '123'

class DevelopmentConfig(BaseConfiguration):
    DEBUG = True
    ENV = 'dev'
    TEMPLATES_AUTO_RELOAD = True

class ProductionConfig(BaseConfiguration):
    DEBUG = False
    TESTING = True
    ENV = 'production'

config_obj = {
    'dev': 'app.config.DevelopmentConfig',
    'prod': 'app.config.ProductionConfig'
}

def configure_app(app):
    """ Configure the Flask WSGI Instance according the enviroment Variable FLASK_CONF """
    enviroment = os.getenv('FLASK_CONFIG', 'dev')
    app.config.from_object(config_obj[enviroment])