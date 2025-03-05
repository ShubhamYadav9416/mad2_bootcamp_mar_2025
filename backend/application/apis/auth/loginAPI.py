from flask import jsonify
import secrets
from flask_security import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token


from application.data.models import db, User, Role, UserRoles

user_post_args = reqparse.RequestParser()
user_post_args.add_argument(
    "email", type=str, required=True, help="user email is required"
)
user_post_args.add_argument(
    "password", type=str, required=True, help="password is req."
)


class LoginAPI(Resource):
    def post(self):
        try:
            args = user_post_args.parse_args()
            email = args.get("email")
            password = args.get("password")

            user = User.query.filter_by(email=email).first()

            if user is None:
                return jsonify({"status": "failed", "message": "User doesn't exist"})

            if not check_password_hash(user.password, password):
                return jsonify({"status": "failed", "message": "wrong password"})

            access_token = create_access_token(identity=user.id)

            login_user(user)

            return jsonify(
                {
                    "status": "success",
                    "message": "You are now login",
                    "access_token": access_token
                }
            )
        except Exception as e:
            print(e)
            return jsonify({"status": "failed", "message": "we dont know why"})


# {
#   "email":"shubham@gmail.com",
#   "password":"123456",
#   "role":"ADMIN",
#   "name":"shubham"
# }
