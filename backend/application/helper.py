from functools import wraps
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import jsonify

from .data.models import  db,UserRoles, Role

def role_required(required_role):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            user_id = int(get_jwt_identity())
            
            user_role = db.session.query(UserRoles).filter_by(user_id=1).first()
            
            if user_role:
                role_id =  user_role.role_id
                
                role_name = Role.query.filter_by(id = role_id).first().name
                
                if required_role != role_name:
                    return jsonify({"status": "failed", "message": "Unauthorized: Insufficient permissions"})
                return fn(*args, **kwargs)
            else: 
                return jsonify({"status": "failed", "message": "Unauthorized: Nothing can be done"})

        return wrapper
    return decorator

            
            
            