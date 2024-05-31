#!/usr/bin/env python3
""" Flask application module """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Optional


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
def get_locale():
    """ Gets client's locale/region
        Checks if locale has been passed in the parameters
    """
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user() -> Optional[Dict]:
    """ Search for user in user database based
        on request id
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id), None)
    return None


@app.before_request
def before_request() -> None:
    """ Do this before serving the
        request
    """
    g.user = get_user()


@app.route("/")
def home():
    """ Home route """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

