from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = str(uuid.uuid4()) # generating a random secret key at app startup

db = SQLAlchemy(app)

from application import routes