
from flask import Blueprint
from flask_login import LoginManager

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_folder='static')

from . routes import *