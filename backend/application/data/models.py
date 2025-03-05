from .database import db
from flask_security import UserMixin, RoleMixin

UserRoles = db.Table(
    "UserRoles",
    db.Column("user_id", db.ForeignKey("user.id")),
    db.Column("role_id", db.ForeignKey("role.id")),
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(199), nullable=False, unique=True)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(199), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean)

    fs_uniquifier = db.Column(db.String(250), unique=True, nullable=False)

    roles = db.relationship("Role", secondary=UserRoles, 
                            backref=db.backref("users"))


# one-to-many
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(199), nullable=False)
    # books = db.relationship("Book", backref="author")


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(199))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))


# many-to-many
student_course = db.Table(
    "student_course",
    db.Column("student_id", db.Integer, db.ForeignKey("student.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id"), primary_key=True),
)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(199), nullable=False)
    courses = db.relationship(
        "Course", secondary=student_course, backref=db.backref("student")
    )


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(199))