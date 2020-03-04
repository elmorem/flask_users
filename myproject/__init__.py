import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Create a login manager object
login_manager = LoginManager()

app = Flask(__name__)
