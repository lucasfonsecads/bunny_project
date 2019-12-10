from flask import Blueprint, request
from flask_restful import Resource, Api
from project.api.models import Users
from project import db


users_blueprint = Blueprint("users", __name__)
api = Api(users_blueprint)


class UsersTest(Resource):
    def get(self):
        return {"status": "success"}

api.add_resource(UsersTest, "/users")        
