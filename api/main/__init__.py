from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from main.config import Config
import pyodbc

app = Flask(__name__)
app.config.from_object(Config)
app.static_folder = Config.STATIC_FOLDER_LOCATION
app.template_folder = Config.TEMPLATE_FOLDER_LOCATION

CORS(app)
db = SQLAlchemy(app)

from main.parking_api import *