from app.modules.users import users_bp
from flask import request, render_template, redirect, url_for
from app.modules.users.user_form import UserRegistrationForm
from app.db.models import User
from flask import flash
from app.db.repositories.BaseOperations import BaseDbOperations
import uuid
from app.db.cryptography import Bcrypt
from app.services.s3 import UploadFile

@users_bp.route('/register', methods=['POST', 'GET'])
def register_user():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user_data = form.data
        try:
            encrypted_password = Bcrypt.password_hash(user_data['password'])
        except Exception as e:
            print(e)
            print('Erro no Encrypt')

        try:
            s3_link = UploadFile().sendToS3(form.data['avatar'], 'UserAvatar')

        except Exception as e:
            print(e)
            print('Erro subindo arquivo pro S3')
            
        new_user = {
            'username': form.data['username'],
            'email': form.data['email'],
            'password': encrypted_password,
            'admin': False,
            'role': form.data['role'].upper(),
            'avatar': s3_link,
            'user_uuid': uuid.uuid4()
        }

        try:
            BaseDbOperations(User).add(new_user)
        except Exception as e:
            print(e)
            flash('Could not create your user, please try again', 'danger')

            return render_template('register_user.html', title='Register User', form=form)

        flash(f"{new_user['username']} Your account has been created succesfully!","success")
        return redirect(url_for('users_bp.login_user'))

    return render_template('register_user.html', title='Register User', form=form)
