"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#SECREAT KEY
app.config['SECRET_KEY'] = '\x81I\xcb\xef\x10\xbb\xe5\xa5\xfdP\x17_\xdf2\x10\xe2mUv\xf1\x01_\xc8\x05\x85}\xe6\xe0M\xcb\xb1+'
#Database URL
app.config["SQLALCHEMY_DATABASE_URL"]='postgresql://postgres:123@localhost:5432/Aginfo'
db=SQLAlchemy(app)



import AgricultureInformationSystem.views

