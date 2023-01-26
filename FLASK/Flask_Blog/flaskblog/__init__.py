#initializing app and bringing together diff components
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# MAIN STARTER FUNCTION
app = Flask(__name__)

# secret key is needed to keep the client-side sessions secure
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# specify location for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # relative path from current file

db = SQLAlchemy(app)  # database instance
bcrypt = Bcrypt(app)  #passwords

from flaskblog import routes