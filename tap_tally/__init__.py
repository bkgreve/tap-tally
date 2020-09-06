from flask import Flask


app = Flask(__name__)

@app.route('/api/entries')
def get_tap_entries():
    return {
        'entries': [
            {
                'beerName': 'Nut Brown Ale',
                'alcByVol': 5.6,
                'beerSRM': 2,
                'beerIBU': 22.1,
                'brewedOn': 'Jan. 20, 2020',
                'keggedOn': 'Feb. 10, 2020',
                'kegNo': 1,
                'tapNo': 1,
                'beerDescription': "Styled after a Southern English brown ale, this ale is dark in color and rich in flavor. It's mild enough for light beer drinkers, but characterful enough for more experienced brewers and beer lovers."
            },
        ]
    }


@app.route('/api/header-info')
def get_header_info():
    return {
        'headerInfo': {
            'breweryName': 'Gypsy Cat Brewing',
            'kegeratorTemp': None
        }
    }
