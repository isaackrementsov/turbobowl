from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db

from app.mod_user.forms import LoginForm
from app.mod_user.models import User


mod_user = Blueprint('user', __name__, url_prefix='/user')


@mod_user.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.findByEmailorUsername(form.emailOrUsername.data)

        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id

            return redirect(url_for('user.home'))

        flash('Wrong username or password', 'error-message')

    return render_template('user/login.html', form=form)
