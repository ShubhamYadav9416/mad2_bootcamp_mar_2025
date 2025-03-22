from datetime import timedelta

SECRET_KEY = 'SHUBHAM'
SQLALCHEMY_DATABASE_URI = 'sqlite:///../db_directory/ourdatabase.db'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours= 1)