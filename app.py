from flask import Flask, render_template
from flask_s3 import FlaskS3
import requests

app = Flask(__name__)
app.config['FLASKS3_BUCKET_NAME'] = 's3-bucket-for-flask'
s3 = FlaskS3(app)

@app.route("/")
def home():
    data = {
        "title": "Flask WebApp",
        "body": "Flask Serverless WebApp"
    }
    return render_template('index.html', data=data)

@app.route("/chuck-norris")
def chuckNorris():
    req = requests.get("http://api.icndb.com/jokes/random/")
    data = {
        "title": "Chuck Norris Joke",
        "api": req.json()
    }
    return render_template('chuck-norris.html', data=data)


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
