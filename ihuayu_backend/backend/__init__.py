from decouple import config as en_var
from flask import Flask
from flask_bcrypt import Bcrypt


def create_app():
    app = Flask(__name__)
    f_bcrypt = Bcrypt()
    # Encrepted with Environment Variable
    app.config['SECRET_KEY'] = en_var('ihuayu', 'ihuayusecret')

    return app
