from app.modules.users import users_bp
from flask import request, render_template
from app.modules.users.user_form import UserRegistrationForm
from app.db.models import User
from flask import flash
from app.db import db

users = [
    {
        'username': 'Matheus',
        'email': 'matheusdev20@gmail.com',
        'admin': True,
        'avatar': None,
        'password': 'Abobrinha',
        'role': 'MANAGER'
    }
]

@users_bp.route('/register', methods=['POST', 'GET'])
def register_user():
    form = UserRegistrationForm()

    if form.validate_on_submit():
        user_data = form.data
        new_user = {
            'username': form.data['username'],
            'email': form.data['email'],
            'password': form.data['password'],
            'admin': form.data['admin'],
            'role': form.data['role'].upper(),
            'avatar': 'RandomS3String'
        }
        db.session.add(User(**new_user))
        db.session.commit()

    return render_template('register_user.html', title='Register User', form=form)
