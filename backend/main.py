from flask import Flask 
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS


from application.data.database import db
from application.data.models import *
import application.config as config

from application.security import security, user_datastore


from application.apis.auth.registerAPI import RegisterAPI
from application.apis.auth.loginAPI import LoginAPI
from application.apis.studentCourse.studentCourseAPI import AllStudentCourseAPI
from application.apis.studentCourse.studentCourseAPI import StudentCourseAPI
from application.apis.roleAPI import RoleAPI
from application.apis.checkPageAccessAPI import CheckPageAccessAPI


app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()

CORS(app, supports_credentials=True)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response

db.init_app(app)
api = Api(app)
api.init_app(app)

JWTManager(app)

security.init_app(app,user_datastore)


api.add_resource(RegisterAPI, "/api/register")
api.add_resource(LoginAPI, "/api/login")
api.add_resource(AllStudentCourseAPI,"/api/studentCourse")
api.add_resource(StudentCourseAPI,"/api/studentCourse/<int:id>")
api.add_resource(RoleAPI, "/api/role")
api.add_resource(CheckPageAccessAPI, "/api/check_page_access")


with app.app_context():
    db.create_all()
    
    
    
if __name__ == "__main__":
    app.run(host="localhost", port=8081, debug = True)

