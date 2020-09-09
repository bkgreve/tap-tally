import os
import json

from flask import Flask


app = Flask(__name__)

@app.route('/api/entries')
def get_tap_entries():
    with open('/usr/src/app/data/beers.json') as f:
        beer_data = json.load(f)
    entries = []
    for entry in beer_data:
        entries.append(entry)
    return {
        'entries': entries
    }


@app.route('/api/header-info')
def get_header_info():
    return {
        'headerInfo': {
            'breweryName': '',
            'kegeratorTemp': None
        }
    }
