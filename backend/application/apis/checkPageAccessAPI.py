from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import  get_jwt_identity, jwt_required
from ..helper import role_required




class CheckPageAccessAPI(Resource):
    @role_required("admin")
    def get(resource): 
        return jsonify({"status":"success", "message":"Role is added"})
