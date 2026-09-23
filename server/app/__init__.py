from flask import Flask 
from .db import db,migrate 
from .config import Config

def create_app():
    app=Flask(__name__)

    app.config.from_object(Config)

    migrate.init_app(app,db)
    db.init_app(app)

    return app