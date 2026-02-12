import os
import pymysql

# 🔹 Make PyMySQL act like MySQLdb (Windows fix)
pymysql.install_as_MySQLdb()

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@localhost/billing'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT (can stay even if not used)
    JWT_SECRET_KEY = '114c9d0510be3c3b856ead1a7d8856be00b21b5b5486c6aadcd1b1746b98cac6'

    # File upload configuration
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'docx', 'xlsx'}
