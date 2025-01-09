from flask import Flask
from flask_mail import Mail
from .config import Config
from .routes import main

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)
    app.register_blueprint(main)

    return app
