from flask import Blueprint# class Blueprint from flask

# creating an instance of blueprint
main = Blueprint('main',__name__)# first argument: name of blueprint , second argument:location of blueprint

from . import views# from this folder import views

# registering the blueprint

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations similar to the one on the main init file
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions this affect the app
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
