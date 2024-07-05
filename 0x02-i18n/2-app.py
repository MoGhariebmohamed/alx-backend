#!/usr/bin/env python3
"""
this is flask configuration
"""
from flask_babel import Babel
from flask import Flask, render_template


class Config(object):
    """
    to configrate the babel app
    """
    LANGUAGES =["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    to get and detrmine the locator
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    index to handle the route
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
