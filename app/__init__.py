from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://worm:worm@localhost/worm"
db = SQLAlchemy(app)

db.create_all()
from app import views,models
