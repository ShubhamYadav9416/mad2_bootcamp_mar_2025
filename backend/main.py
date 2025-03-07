from flask import Flask 
from flask_restful import Api
from flask_jwt_extended import JWTManager


from application.data.database import db
from application.data.models import *
import application.config as config

from application.security import security, user_datastore


from application.apis.auth.registerAPI import RegisterAPI
from application.apis.auth.loginAPI import LoginAPI
from application.apis.studentCourse.studentCourseAPI import AllStudentCourseAPI
from application.apis.studentCourse.studentCourseAPI import StudentCourseAPI


app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()

db.init_app(app)
api = Api(app)
api.init_app(app)

JWTManager(app)

security.init_app(app,user_datastore)


api.add_resource(RegisterAPI, "/api/register")
api.add_resource(LoginAPI, "/api/login")
api.add_resource(AllStudentCourseAPI,"/api/studentCourse")
api.add_resource(StudentCourseAPI,"/api/studentCourse/<int:id>")


with app.app_context():
    db.create_all()
    
if __name__ == "__main__":
    app.run(host="localhost", port=8081, debug = True)

