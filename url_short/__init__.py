from flask import Flask

from .extensions import db #. since both are in same folder
from url_short.routes import short

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(short)
    
    return app