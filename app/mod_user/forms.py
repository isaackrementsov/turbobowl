import os
import uuid

from flask import current_app
from flask_wtf import FlaskForm
from flask_wtf.file import FileField

from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email


class LoginForm(FlaskForm):

    emailOrUsername = TextField('EmailAddressOrUsername', [Required()])
    password = PasswordField('Password', [Required()])


class SignupForm(FlaskForm):

    email = TextField('Email', [Required(), Email()])
    username = TextField('Username', [Required()])
    password = PasswordField('Password', [Required()])
    avatar = FileField()

    def save_avatar(self):
        filename_original = self.avatar.data.filename
        ext = filename_original.split('.')[-1]

        filename_new = str(uuid.uuid4()) + ext

        self.avatar.data.save(os.path.join(current_app.config['BASE_DIR'], 'app/static/img/upload', filename_new))

        return filename_new
