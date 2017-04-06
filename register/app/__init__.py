from flask import Flask, redirect
from config import DevConfig
from app.models import db

app = Flask(__name__)
# Set the app config
app.config.from_object(DevConfig)
from app import views

# Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
db.init_app(app)
