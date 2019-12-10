from flask_restful import Resource, reqparse
from flask import request
from project.api.models import Users
from project import db


class CreateUser(Resoure):
    def post(self):
        new_user = Users(
            name = data["name"]
        )

        try:
            db.session.add(new_user)
            db.session.commit()

            return {
                "message": "User {} was created".format(data["name"])
            }, 200
        
        except:
            return {"message": "Something went wrong"}, 500    