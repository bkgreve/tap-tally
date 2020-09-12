import os

from flask import Flask


def create_app(test_config=None):
    """Flask Application Factory"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('FLASK_SECRET_KEY', 'changeme'),
        DATABASE=os.path.join(app.instance_path, 'tap-tally.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register blueprints for different modules
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .control_center import control_center as control_blueprint
    app.register_blueprint(
        control_blueprint, url_prefix='/control-center'
    )

    return app
