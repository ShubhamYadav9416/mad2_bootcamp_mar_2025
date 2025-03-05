from flask import jsonify
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, reqparse


from application.data.models import db, User, Role, UserRoles

user_post_args = reqparse.RequestParser()
user_post_args.add_argument(
    "email", type=str, required=True, help="user email is required"
)
user_post_args.add_argument(
    "name", type=str, required=True, help="user name is required"
)
user_post_args.add_argument(
    "password", type=str, required=True, help="password is req."
)
user_post_args.add_argument("role", type=str, required=True, help="role is required")


class RegisterAPI(Resource):
    def post(self):
        try:
            args = user_post_args.parse_args()
            email = args.get('email')
            password = args.get('password')
            name = args.get('name')
            role = args.get('role')
            
            user = User.query.filter_by(email = email).first()
            
            if user:
                return jsonify({"status":"failed", "message": "User already exist"})
            
            user_role = Role.query.filter_by(name = role).first()
            print(user_role)
            if user_role is None:
                return jsonify({"status":"failed", "message": "Role doesn't exist"})
            
            hash_password = generate_password_hash(password)
            
            new_user = User(email=email, name = name, password = hash_password)
            new_user.roles.append(user_role)
            new_user.fs_uniquifier = secrets.token_hex(16)
            db.session.add(new_user)
            db.session.commit()
            
            return jsonify({"status":"success", "message": "You are now registered"})
        except Exception as e:
            print(e)
            return jsonify({"status":"failed", "message": "we dont know why"})
        
        
        
# {
#   "email":"shubham@gmail.com",
#   "password":"123456",
#   "role":"ADMIN",
#   "name":"shubham"
# }
