from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.db'
app.config['SECRET_KEY'] = "220220144245231423Jadufnesdjb"
db = SQLAlchemy(app)

from static import routes