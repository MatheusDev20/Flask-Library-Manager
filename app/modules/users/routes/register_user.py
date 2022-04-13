from app.modules.users import users_bp
from flask import request, render_template
from app.modules.users.user_form import UserRegistrationForm

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
        print(form.errors)
        print(form.data)

    print(form.errors)
    return render_template('register_user.html', title='Register User', form=form)
