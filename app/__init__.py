from flask import Flask

from flask_bootstrap import Bootstrap
from config import config_options

#making an instance of bootstrap
bootstrap = Bootstrap()

def create_app(config_name):
    # instance of flask
    app = Flask(__name__)

    # app configs
    app.config.from_object(config_options[config_name])

    # flask extensions
    bootstrap.init_app(app)

    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting up the configuration
    from .request import configure_request
    configure_request(app)

    return app
