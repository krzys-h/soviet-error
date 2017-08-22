# soviet-error

A tool to preprocess error messages to be sung by Festival song synthesizer to various melodies.

## Installation

* `virtualenv venv`
* `. venv/bin/activate`
* `pip install -r requirements.txt`

## Usage
`python synthesize.py MELODY MESSAGE | festival --pipe`

where melody is:

* `USSR` (USSR Anthem),
* `Internationale` (The Internationale),
* `WKNP` (a Polish folk melody, "Wlazł kotek na płotek").

Example:

`echo "An error occured and the world is on fire" | python synthesize.py USSR | festival --pipe`


