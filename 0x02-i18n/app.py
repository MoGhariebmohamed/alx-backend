#!/usr/bin/env python3
"""
this is flask configuration
"""
import locale
from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import Dict, Union
from datetime import datetime
from datetime import timezone as tmzn
from pytz import timezone
import pytz.exceptions


class Config(object):
    """
    to configrate the babel app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Returns a user dictionary or None if ID value
    """
    user_id = request.args.get('login_as', None)
    if user_id and int(user_id) in users.keys():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Add user to flask.g if user is found
    """
    user = get_user()
    g.user = user
    time_now = pytz.utc.localize(datetime.utcnow())
    time = time_now.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    fmt = "%b %d, %Y %I:%M:%S %p"
    g.time = time.strftime(fmt)


@babel.localeselector
def get_locale():
    """
    to get and detrmine the locator
    """
    locator = request.args.get('locale')
    if locator in app.config['LANGUAGES']:
        return locator
    if g.user:
        locator = g.user.get('locale')
        if locator and locator in app.config['LANGUAGES']:
            return locator
    locator = request.headers.get('locale', None)
    if locator in app.config['LANGUAGES']:
        return locator
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Select and return appropriate timezone
    """
    timezone = request.args.get('timezone', None)
    if timezone:
        try:
            return timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            timezone = g.user.get('timezone')
            return timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    dflt = app.config['BABEL_DEFAULT_TIMEZONE']
    return dflt


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    index to handle the route
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)