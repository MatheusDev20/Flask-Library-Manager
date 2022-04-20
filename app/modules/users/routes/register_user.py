from app.modules.users import users_bp
from flask import request, render_template, redirect, url_for
from app.modules.users.user_form import UserRegistrationForm
from app.db.models import User
from flask import flash
from app.db.repositories.BaseOperations import BaseDbOperations

@users_bp.route('/register', methods=['POST', 'GET'])
def register_user():
    form = UserRegistrationForm()

    if form.validate_on_submit():
        user_data = form.data
        new_user = {
            'username': form.data['username'],
            'email': form.data['email'],
            'password': form.data['password'],
            'admin': False,
            'role': form.data['role'].upper(),
            'avatar': 'RandomS3String'
        }

        BaseDbOperations(User).add(new_user)
        flash(f"{new_user['username']} Your account has been created succesfully!")
        return redirect(url_for('users_bp.login_user'))

    print(form.errors)
    return render_template('register_user.html', title='Register User', form=form)
