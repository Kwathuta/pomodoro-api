from flask_restful import Api
from flask import Blueprint

version1 = Blueprint("v1", __name__, url_prefix="/api/v1")
api = Api(version1, catch_all_404s=True)

from app.auth.v1.views.user_views import User, UserSearch

api.add_resource(User, "/auth/users")
api.add_resource(UserSearch, "/auth/users/<id>")
