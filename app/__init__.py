from flask import Flask
from app.config import configure_app
from flask import current_app

def create_app():
    """ Instance and create Flask WSGI App """
    app = Flask(__name__)
    configure_app(app)

    with app.app_context():
        @app.route('/')
        def first_route():
            return 'Hello Application Change'

    return app


