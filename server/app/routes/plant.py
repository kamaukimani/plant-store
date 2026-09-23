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
    def post(self):
        data=request.get_json()

        plant=Plant()
        allowed_fields=["name","image","price"]

        for attr in data:
            if attr in allowed_fields:
                setattr(plant,attr,data[attr])
        db.session.add(plant)
        db.session.commit()

        plant_dict=plant.to_dict()

        response=make_response(
            plant_dict,
            201
        )
        return response

class PlantsById(Resource):
    def get(self,id):
        plant=Plant.query.filter(Plant.id == id).first()
        if plant is None:
            return {
                "message":"OOOOpppss!!!The plant does not exist in our database"
            },404
        plant_dict=plant.to_dict()
        response=make_response(
            plant_dict,
            200
        )
        return response
    def patch(self,id):
        plant=Plant.query.filter_by(id=id).first()
        if plant is None:
            return {
                "message":"OOOOpppss!!!The plant does not exist in our database"
            },404
        data=request.get_json()
        allowed_fields=["name","price"]

        for attr,value in data.items():
            if attr in allowed_fields:
                setattr(plant,attr,value)
        db.session.commit()
        plant_dict=plant.to_dict()
        response=make_response(
            plant_dict,
            200
        )
        return response
    def delete(self,id):
        plant=Plant.query.filter_by(id=id).first()
        if plant is None:
            return {
                "message":"OOOOpppss!!!The plant does not exist in our database"
            },404
        db.session.delete(plant)
        db.session.commit()

        response={
            "deleted_successfully":True,
            "message":"The plant has been successfully deleted"
        }
        return response,200

