from flask_restful import Resource 
from flask import make_response,request 
from app.models import Plant
from app.db import db

class Plants(Resource):
    def get(self):
        plants=[plant.to_dict() for plant in Plant.query.all()]
        response=make_response(
            plants,
            200
        )
        return response
    