import os
import json

from . import api


@api.route('/entries')
def get_tap_entries():
    """API Endpoint for returning Tap Entries to display"""
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


@api.route('/header-info')
def get_header_info():
    """API Endpoint for returning information for Header"""
    return {
        'headerInfo': {
            'breweryName': 'Gypsy Cat Brewing!',
            'kegeratorTemp': None
        }
    }
