import os
import json

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

    @app.route('/api/entries')
    def get_tap_entries():
        with open('/usr/src/app/data/beers.json') as f:
            beer_data = json.load(f)
        entries = []
        for entry in beer_data:
            if entry.get('visible', False):
                image_name = entry.get('image', False)
                if image_name:
                    image_exists = os.path.exists(f"/usr/src/app/data/images/{image_name}")
                    if not image_exists:
                        entry['image'] = None
                entries.append(entry)
        return {
            'entries': entries
        }


    @app.route('/api/header-info')
    def get_header_info():
        return {
            'headerInfo': {
                'breweryName': 'Gypsy Cat Brewing',
                'kegeratorTemp': None
            }
        }

    return app
