"""
Initial setup of the app.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

import os

from dotenv import dotenv_values
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# Load environment variables
config = dotenv_values(".env")
if not config:
    config = dict(os.environ)
try:
    FLASK_DEBUG = str(config["FLASK_DEBUG"]) == "True"
    SECRET_KEY = str(config["PV_SECRET_KEY"])
    if not SECRET_KEY:
        error_message = "PV_SECRET_KEY is empty. Did you update the environment variables?"
        raise ValueError(error_message)

    PRIVATE_LECTURE_AUTOMATION = str(config["PRIVATE_LECTURE_AUTOMATION"]) == "True"
    CHECKMARK = str(config["CHECKMARK"]) == "True"
except KeyError as e:
    error_message = "Config variables are missing. Check .env file or add environment variables."
    raise KeyError(error_message) from e

# Create the app
app = Flask(__name__)
app.config["FLASK_DEBUG"] = FLASK_DEBUG
app.config["SECRET_KEY"] = SECRET_KEY

app.config["SESSION_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = True

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

app.config["PRIVATE_LECTURE_AUTOMATION"] = PRIVATE_LECTURE_AUTOMATION
app.config["CHECKMARK"] = CHECKMARK

csrf = CSRFProtect(app)
db = SQLAlchemy(app)

from pythonvilag_website import routes  # noqa: E402, F401
