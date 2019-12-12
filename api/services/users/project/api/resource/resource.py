from flask_restful import Resource, reqparse
from flask import request
from project.api.models import Users, Tasks
from project import db

#Class to create one user
class CreateUser(Resource):
    def post(self):
        data = request.get_json()
        new_user = Users(
            name= data["name"]
        )

        try:
            db.session.add(new_user)
            db.session.commit()

            return{
                "message": "User {} was created".format(data["name"]),
            }, 200

        except ValueError:
            return {"message": "Something went wrong"}, 500    

class CreateTask(Resource):
    def post(self):
        data = request.get_json()

        current_user = Users.query.filter_by(name=data["name"]).first()
        
        new_task = Tasks(
            description = data["description"],
            user_id = current_user.id,
            status = data["status"]
        )

        try:
            db.session.add(new_task)
            db.session.commit()

            return { "message": "task create" }, 200
        
        except:
            return {"message": "Something went wrong"}, 500

class AllTaskUser(Resource):
    def post(self):
        data = request.get_json()

        current_user = Users.query.filter_by(name=data["name"]).first()

        tasks_user = Tasks.query.filter_by(user_id=current_user.id).all()
        
        response_object = {
                "data": {"tasks": [tasks.to_json() for tasks in tasks_user]}
            }

        return response_object, 200

class ChangeStatus(Resource):
    def post(self):
        data = request.get_json()

        task_user = Tasks.query.filter_by(id=data["task_id"]).first()

        try:
            task_user.status = data["status"]
            db.session.commit()
            return { "message": "task change status" }, 200
        
        except:
            return {"message": "Something went wrong"}, 500


class ShowUser(Resource):
    def get(self):
        try:
            currents_users = Users.query.all()

            response_object = {
                "data": {"users": [users.to_json() for users in currents_users]}
            }
            return response_object, 200

        except ValueError:
            return ValueError

class ShowTasks(Resource):
    def get(self):
        try:
            currents_tasks = Tasks.query.all()

            response_object = {
                "data": {"tasks": [tasks.to_json() for tasks in currents_tasks]}
            }
            return response_object, 200

        except ValueError:
            return ValueError        
