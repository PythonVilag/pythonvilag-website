"""
Initial setup of the app.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

import os

from dotenv import dotenv_values
from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

config = dotenv_values(".env")
if not config:
    config = dict(os.environ)
try:
    SECRET_KEY = str(config["PV_SECRET_KEY"])
    FLASK_DEBUG = True if str(config["FLASK_DEBUG"]) == "True" else False
except KeyError as e:
    raise KeyError(
        "Config variables are missing. Check .env file or add environment variables."
    ) from e

app = Flask(__name__)
app.config["CACHE_TYPE"] = "simple"
app.config["FLASK_DEBUG"] = FLASK_DEBUG
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Strict"
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

cache = Cache(app)
csrf = CSRFProtect(app)
db = SQLAlchemy(app)

from pythonvilag_website import routes  # noqa: E402, F401
