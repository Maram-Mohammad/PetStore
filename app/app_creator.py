from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import app_settings

db = SQLAlchemy()

def create_app(app_name):

    app = Flask(app_name, instance_relative_config=True)
    app.config.update(app_settings)
    db.init_app(app)
    app.db = db    
    return app