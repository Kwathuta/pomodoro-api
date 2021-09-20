from app.auth.v1.models.user_models import UserModels
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

parser = RequestParser()

parser.add_argument("task", type=str, required=True, help="Please input task")
parser.add_argument("username", type=str, required=True, help="Please input username")
parser.add_argument(
    "task_timer", type=int, required=True, help="Please input valid time in minutes"
)
parser.add_argument(
    "break_timer", type=int, required=True, help="Please input valid time in minutes"
)
parser.add_argument(
    "task_completed",
    type=bool,
    required=True,
    help="Please input whether True or False",
)


class User(Resource):
    """
    User endpoints
    """

    def post(self):
        """
        Register a user endpoint
        """
        args = parser.parse_args()
        args = request.get_json()
        task = args["task"]
        username = args["username"]
        task_timer = args["task_timer"]
        break_timer = args["break_timer"]
        task_completed = args["task_completed"]

        newUser = UserModels(username, task, task_timer, break_timer, task_completed)
        newUser.save_user()

        return {
            "message": "User registered successfully, timer begins now",
            "user": newUser.__dict__,
        }, 201

    def get(self):

        return {
            "user": UserModels.users,
        }


class UserSearch(Resource):
    def get(self, id):
        user_id = int(id) - 1

        return {
            "user": UserModels.users[user_id],
        }
