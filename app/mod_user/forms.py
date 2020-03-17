from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email


class LoginForm(FlaskForm):

    emailOrUsername = TextField('EmailAddressOrUsername', [Required()])
    password = PasswordField('Password', [Required()])
