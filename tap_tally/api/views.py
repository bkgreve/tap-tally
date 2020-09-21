import os
import json
import logging

from . import api
from ..models.tap_entry import TapEntry
from .. import db


@api.route('/entries')
def get_tap_entries():
    """API Endpoint for returning Tap Entries to display"""
    tap_entires = TapEntry.query.filter(TapEntry.visible == True)
    entries = []
    for entry in tap_entires:
        brewed = entry.brewed_on.strftime('%b. %d, %Y')
        kegged = None
        if entry.kegged_on:
            kegged = entry.kegged_on.strftime('%b. %d, %Y')
        display_entry = {
            "tapNo": entry.tap_number,
            "alcByVol": entry.alc_by_vol,
            "beerName": entry.name,
            "beerSRM": entry.srm,
            "beerIBU": entry.ibu,
            "brewedOn": brewed,
            "keggedOn": kegged,
            "kegNo": entry.keg_no,
            "beerDescription": entry.description,
            "image": False
        }
        entries.append(display_entry)
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
