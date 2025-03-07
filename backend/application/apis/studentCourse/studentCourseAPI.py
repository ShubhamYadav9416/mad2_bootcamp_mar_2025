from flask import request, jsonify
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from flask_jwt_extended import jwt_required


from application.data.models import db, Course, Student, StudentCourse

student_course_post_args = reqparse.RequestParser()
student_course_post_args.add_argument("course_name", type=str, required = True, help = "Course name is req.")
student_course_post_args.add_argument("student_name", type=str, required = True, help = "Student name is req.")



class AllStudentCourseAPI(Resource):
    def get(resource):  # getting all the data
        all_records = (
            StudentCourse.query.join(Course, StudentCourse.course_id == Course.id)
            .join(Student, StudentCourse.student_id == Student.id)
            .add_columns(Student.id, Course.id, Student.name, Course.name)
            .all()
        )
        print(all_records)
        data = []
        for record in all_records:
            entry = {}
            entry["student_id"] = record[1]
            entry["course_id"] = record[2]
            entry["student_name"] = record[3]
            entry["course_name"] = record[4]
            data.append(entry)
        print(data)
        return data


    def post(resource):
        args = student_course_post_args.parse_args()
        student_name = args.get("student_name")
        course_name = args.get("course_name")
        
        course = Course.query.filter_by(name = course_name).first()

        if course is None:
            course = Course(name = course_name)
            db.session.add(course)
            db.session.commit()
        course_id = course.id
        
        
        student = Student.query.filter_by(name = student_name).first()
        if student is None:
            student = Student(name = student_name)
            db.session.add(student)
            db.session.commit()
        student_id = student.id
        
        
        new_student_course = StudentCourse(student_id=student_id, course_id = course_id)
        db.session.add(new_student_course)
        db.session.commit()
        
        return jsonify({"status":"success", "message":"record is added"})
        
        
        


class StudentCourseAPI(Resource):
    def get(self, id):
        student_course = StudentCourse.query.filter_by(student_course_id = id).first()
        if student_course is None:
            return jsonify({"status":"failed", "message":"no Record Exist"})
        record = {
            "student_course_id": student_course.student_course_id,
            "student_id": student_course.student_id,
            "course_id": student_course.course_id,
            "student_name": Student.query.filter_by(id = student_course.student_id).first().name,
            "course_name": Course.query.filter_by(id = student_course.course_id).first().name
        }
        return jsonify({"status":"success", "message":"Record Exist","data":record})
    
    def delete(self,id):
        student_course = StudentCourse.query.filter_by(student_course_id = id).first()
        if student_course is None:
            return jsonify({"status":"failed", "message":"no Record Exist"})
        db.session.delete(student_course)
        db.session.commit()
        return jsonify({"status":"success", "message":"Record Deleted"})
    
#     def put:





# shubham is in 3 courses already then how to update?
