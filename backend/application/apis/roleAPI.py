from flask import request, jsonify
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from flask_jwt_extended import jwt_required


from application.data.models import db, Role

role_post_args = reqparse.RequestParser()
role_post_args.add_argument("role", type=str, required = True, help = "Role is req.")


resource_fields = {
    "id" : fields.Integer,
    "name" : fields.String
}


class RoleAPI(Resource):
    @marshal_with(resource_fields)
    def get(resource):  # getting all the data
        data = Role.query.all()
        return data


    def post(resource):
        args = role_post_args.parse_args()
        role_name = args.get("role")
        role =  Role.query.filter_by(name = role_name).first()
        
        if role:
            return jsonify({"status":"failed", "message":"role already exist's"})
        
        new_role = Role(name = role_name)
        db.session.add(new_role)
        db.session.commit()
        
        return jsonify({"status":"success", "message":"Role is added"})
        
        
    






