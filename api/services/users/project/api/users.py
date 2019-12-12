from flask import Blueprint, request
from flask_restful import Resource, Api
from project.api.models import Users
from project import db
from project.api.resource.resource import (
    CreateUser,
    CreateTask,
    ShowUser,
    ShowTasks,
    AllTaskUser,
    ChangeStatus
)


users_blueprint = Blueprint("users", __name__)
api = Api(users_blueprint)


class UsersTest(Resource):
    def get(self):
        return {"status": "success"}


api.add_resource(UsersTest, "/users")
api.add_resource(CreateUser, "/users/createUser")
api.add_resource(CreateTask, "/users/createTask")
api.add_resource(ShowUser, "/users/showAllUsers")
api.add_resource(ShowTasks, "/users/showTasks")
api.add_resource(AllTaskUser, "/users/allUserTask")
api.add_resource(ChangeStatus, "/users/changeStatus")
