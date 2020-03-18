from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.controllers import missing_session, go_home, go_user_home

from app.mod_user.forms import LoginForm, SignupForm
from app.mod_user.models import User


mod_user = Blueprint('user', __name__, url_prefix='/user')


def create_session(user):
    session['user_id'] = user.id
    session['username'] = user.username
    session['avatar'] = user.avatar


@mod_user.route('/login/', methods=['GET', 'POST'])
def login():
    if not missing_session(): return go_user_home()

    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.find_by_email_or_username(form.emailOrUsername.data)

        if user and user.password == form.password.data:
            create_session(user)

            return redirect(url_for('user.profile', user_id=user.id))

        flash('Wrong username or password', 'error')

    return render_template('user/login.html', form=form, session=session)


@mod_user.route('/signup/', methods=['GET', 'POST'])
def signup():
    if not missing_session(): return go_user_home()

    form = SignupForm()

    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)

        if form.avatar.data is not None:
            user.avatar = form.save_avatar()

        try:
            user.save()

            create_session(user)

            return redirect(url_for('user.profile', user_id=user.id))
        except Exception as e:
            field = str(e).split('.')[2].split('[')[0]

            flash('Please choose a unique ' + field, 'error')

    return render_template('user/signup.html', form=form, session=session)


@mod_user.route('/<user_id>', methods=['GET'])
def profile(user_id):
    if missing_session(): return go_home()

    user = User.query.get(user_id)

    return render_template('user/profile.html', session=session, user=user)


@mod_user.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()

    return redirect(url_for('user.login'))
