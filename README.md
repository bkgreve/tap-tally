# Tap Tally: A Digital Beer List and Keg Level Monitor

Tap Tally is designed to present a list of what's on tap in an aesthetically pleasing manner.
It will also (_in an upcoming release_) interface with flow meters to keep a real-time tally
of current keg levels -- no more running dry at the worst possible moment! Finally, Tap Tally also
(_in an upcoming release_) provides provisions for keeping notes about batches for streamlined record keeping.

_Tap Tally is still very much a work in progress_

## Installation

To quickly get started with Tap Tally:
```sh
git clone git@github.com:bkgreve/tap-tally.git
cd tap-tally
docker-compose up
```

Docker-compose will then build 2 images: one for the Flask back-end that serves the data and then
an Nginx image, which also includes the static assets.

## Usage

### Starting Tap Tally

The `docker-compose up` command will start Tap Tally, and the app can be accessed by navigating to
http://localhost in your browser. Depending on your network configuration, you may also be able to
access Tap Tally from all machines on your network (by default, it is listening on port 80). 

### Editing the tap list

Currently, all beer/tap data are stored in `data/beers.json` (_a future release will explore alternative
data storage methods_). This file has the following structure:
```json
[
  {
    "tapNo": 1,
    "alcbyVol": 5,
    "beerName": "Beer Name Here",
    "beerSRM": 1,
    "beerIBU": 1,
    "brewedOn": "Jan. 1, 2020",
    "keggedOn": "Feb. 1, 2020",
    "kegNo": 1,
    "beerDescription": "Beer description goes here",
    "visible": true
  },
  {
    "tapNo": 2,
    "alcbyVol": 5,
    "beerName": "Beer Name Here",
    "beerSRM": 1,
    "beerIBU": 1,
    "brewedOn": "Jan. 1, 2020",
    "keggedOn": "Feb. 1, 2020",
    "kegNo": 1,
    "beerDescription": "Beer description goes here"
  }
]
```
All objects with `visible` set to `true` in the above array will be loaded and passed to the front-end
for display. An example file is included in this repository: simply edit the file with
your favorite editor, save, and then refresh the page to see your changes. You can add as many or as few
beers as you'd like.

Then, navigating to `http://localhost` (once the Docker containers are running) should
show your tap list!

## Screenshots

![image](https://user-images.githubusercontent.com/39656757/92596320-a6186980-f273-11ea-9d93-0ce911e2e213.png)
