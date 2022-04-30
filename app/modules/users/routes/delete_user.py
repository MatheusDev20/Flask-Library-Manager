from app.modules.users import users_bp
from flask import request, render_template, redirect, url_for
from app.modules.users.user_form import UserRegistrationForm
from app.db.models import User
from flask import flash
from app.db.repositories.BaseOperations import BaseDbOperations
import uuid
from app.services.s3 import UploadFile

@users_bp.route('/delete/<user_id>', methods=['GET'])
def delete_user(user_id):
    
    try:
        deleted_user = BaseDbOperations(User).get_by_id(user_id)
        BaseDbOperations(User).exclude(deleted_user['data'])

    except Exception as e:
        print(e)
        print('Erro deletando o usuário')

    return redirect(url_for('users_bp.load_users'))

