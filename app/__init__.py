from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

# Explicitly load the .env file from the app directory
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

# Print the loaded environment variables for debugging
print("DB_URI:", os.getenv('DB_URI'))
print("SECRET_KEY:", os.getenv('SECRET_KEY'))


#load secret key from environment
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


#load database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Check if SQLALCHEMY_DATABASE_URI is set correctly
if not app.config['SQLALCHEMY_DATABASE_URI']:
    raise RuntimeError("SQLALCHEMY_DATABASE_URI is not set. Check your .env file and environment variables.")

db = SQLAlchemy(app)



from app.routes.root import *
from app.routes.admin import *
from app.models.user import *
from app.models.admin import *