from app.modules.home import home_bp
from flask import render_template
from flask_login import login_required

@home_bp.route('/', methods=['GET'])
@login_required
def home():
    return render_template('home.html')