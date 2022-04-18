from app.modules.users import users_bp
from flask import request, render_template
from app.modules.users.user_form import LoginUserForm
from app.db.models import User
from flask import flash
from app.db.repositories.BaseOperations import BaseDbOperations

@users_bp.route('/login', methods=['POST', 'GET'])
def login_user():
    form = LoginUserForm()
    if form.is_submitted():
        print('?')
    return render_template('login.html', title='Login',form=form)