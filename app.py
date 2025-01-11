from flask import Flask
from flask_mail import Mail
from app.config import Config
from app.routes import main

app = Flask(__name__)
