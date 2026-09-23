from flask import Flask 
from .db import db,migrate 
from .config import Config
from .models import *
from flask_restful import Api
from .routes import *

def create_app():
    app=Flask(__name__)

    app.config.from_object(Config)

    migrate.init_app(app,db)
    db.init_app(app)
    api=Api(app)

    api.add_resource(Plants,"/plants")

    return app