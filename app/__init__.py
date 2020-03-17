from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config.from_object('config')


db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



from app.mod_user.controllers import mod_user


app.register_blueprint(mod_user)


db.create_all()
