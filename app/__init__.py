from flask import Flask
from app.config import configure_app
from flask import current_app
from app.db.models import *
from app.db import db
from flask_migrate import Migrate
from app.modules import users_bp, home_bp
import os
from app.modules.users import login_manager

def create_app():
    """ Instance and create Flask WSGI App """
    app = Flask(__name__)
    configure_app(app)
    login_manager.init_app(app)
    
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        app.register_blueprint(users_bp, url_prefix='/user')
        app.register_blueprint(home_bp, url_prefix='/app')

        @app.route('/')
        def first_route():
            return 'Hello Application Change'

    return app


