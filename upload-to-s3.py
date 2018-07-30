import flask_s3
from app import app
flask_s3.create_all(app)
print("All Files Uploaded Successfully!")
