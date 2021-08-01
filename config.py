"""Flask config."""
import os
from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
APP_DIR = os.path.join(BASE_DIR, "apps")
STORAGE_DIR = os.path.join(BASE_DIR, "storage")

UPLOADED_STATEMENTS_ALLOW = ('csv', 'CSV')
UPLOADED_STATEMENTS_DEST = os.path.join(STORAGE_DIR, "uploads")
class Config:
    """Flask configuration variables."""

    # General Config
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    SECRET_KEY = environ.get("SECRET_KEY")

    # Assets
    LESS_BIN = environ.get("LESS_BIN")
    ASSETS_DEBUG = environ.get("ASSETS_DEBUG")
    LESS_RUN_IN_DEBUG = environ.get("LESS_RUN_IN_DEBUG")

    # Static Assets
    # STATIC_FOLDER = "static"
    # TEMPLATES_FOLDER = "templates/public"
    # COMPRESSOR_DEBUG = environ.get("COMPRESSOR_DEBUG")