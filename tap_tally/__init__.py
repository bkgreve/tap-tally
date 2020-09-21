import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    """Flask Application Factory"""
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path='/flask_static/',
        static_folder='flask_static/'
    )

    app.config.from_mapping(
        SECRET_KEY=os.getenv('FLASK_SECRET_KEY', 'changeme'),
        SQLALCHEMY_DATABASE_URI=os.getenv(
            'SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/tap-tally.db'
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    Bootstrap(app)

    # Register blueprints for different modules
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .control_center import control_center as control_blueprint
    app.register_blueprint(
        control_blueprint, url_prefix='/control-center'
    )
    db.create_all(app=app)
    return app
