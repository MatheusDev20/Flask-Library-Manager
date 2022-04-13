
from flask import Blueprint

users_bp = Blueprint('users_bp', __name__, template_folder='templates', static_folder='static')

from .routes import *
from .user_form import *