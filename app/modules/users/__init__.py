
from flask import Blueprint
from flask_login import LoginManager

users_bp = Blueprint('users_bp', __name__, template_folder='templates', static_folder='static')
login_manager = LoginManager()

from .routes import *
from .user_form import *