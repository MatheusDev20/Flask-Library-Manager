from flask_login import login_user, logout_user, login_required
from app.modules.users import users_bp
from flask import request, render_template, redirect, url_for
from app.db.models import User
from app.db.repositories.BaseOperations import BaseDbOperations
from flask import flash
from app.db.cryptography import Bcrypt
from app.utils.UsefulFunctions import UseFullFunctions


@users_bp.route('/users',methods=['GET', 'POST'])
@login_required
def load_users():
    users = BaseDbOperations(User).get_all()
    list_users = [UseFullFunctions.sql_alchemy_to_dict(user) for user in users]

    filtered_data = []
    for user in list_users:
        new_dict = {
            'id': user['id'],
            "username": user['username'],
            "email": user['email'],
            'role': user['role'].split('.')[1]
        }
        filtered_data.append(new_dict)
    
    return render_template('users_list.html', title='Users List', users=filtered_data)