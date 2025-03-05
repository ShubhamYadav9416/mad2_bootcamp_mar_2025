import json
from flask import request, jsonify
from flask_restful import Resource, reqoarse, abort, fields, marshal_with
from flask_jwt_extended import jwt_required


from application.data.models import db, Author

resource_fields = {
    'author_id': fields.Integer,
    'author_name': fields.String
}

class AllAuthorAPI(Resource):
    @marshal_with(resource_fields)
    def get(resource):
        authors = Author.query.all()
        if not authors:
            abort(404, message="no authors found")
        return authors