from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '0000'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/marketeers'
db = SQLAlchemy(app)

# Import your models after initializing db to avoid circular imports
from app import views
