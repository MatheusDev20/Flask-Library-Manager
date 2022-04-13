from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class UserRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    password_confirmation = PasswordField('PasswordConfirmation', validators=[DataRequired(), Length(min=8)])
    admin = BooleanField('Admin', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])

    submit = SubmitField('Register')
