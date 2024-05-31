#!/usr/bin/env python3
""" Flask application module """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Optional
from pytz import exceptions as pytz_exceptions, timezone


class Config(object):
    """ Flask app configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """ Gets client's locale/region
        Checks if locale has been passed in the url
        parameters and user locale preferences
    """
    locale = request.args.get("locale", "")
    if locale in app.config["LANGUAGES"]:
        return locale

    if not g.user:
        return request.accept_languages.best_match(Config.LANGUAGES)

    locale = g.user.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone() -> str:
    """ Check for client's timezone based on
        url parameters and client's preferences
    """
    tz = request.args.get("timezone", '')

    if not tz and g.user:
        tz = str(g.user.get('timezone', ''))

    # Check if timezone is valid
    try:
        return timezone(tz).zone
    except pytz_exceptions.UnknownTimeZoneError as e:
        return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user() -> Optional[Dict]:
    """ 	Method that search 
    for user in user database based
        on request id
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id), None)
    return None


@app.before_request
def before_request() -> None:
    """ Method of what to do before a request
    """
    g.user = get_user()


@app.route("/")
def home():
    """ Home route """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
''
