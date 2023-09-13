#!/usr/bin/env python3
"""
A Basic Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """Represents a flask babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """gets the locale for a web page"""
    queries = request.query_string.decode('utf-8').split('8')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """The index view"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
