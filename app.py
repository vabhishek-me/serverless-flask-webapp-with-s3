from flask import Flask, render_template
from flask_s3 import FlaskS3

app = Flask(__name__)
app.config['FLASKS3_BUCKET_NAME'] = 's3-bucket-for-flask'
s3 = FlaskS3(app)

@app.route("/")
def hello():
    data = {
        "title": "Flask WebApp",
        "body": "Flask Serverless WebApp"
    }
    return render_template('index.html', data=data)
