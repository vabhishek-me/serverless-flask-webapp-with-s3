# Serverless Flask WebApp with S3

Serverless Flask WebApp with S3(for static content like images,css,js etc).

## Installation

- Install [Python3.6](https://www.python.org/downloads/release/python-366/)

- Git clone the repo
```bash
git clone https://github.com/vabhishek-me/serverless-flask-webapp-with-s3.git;
cd serverless-flask-webapp-with-s3;
```

- Install `virtualenv` on your system to create a virtual environment.

  ```bash
  pip3 install virtualenv;
  ```

- Create a virtualenv named `flaskenv` and activate it.

  ```bash
  virtualenv -p python3.6 flaskenv;
  source flaskenv/bin/activate;
  ```

- Install all the dependencies.

  ```bash
  pip install -r requirements.txt
  ```

- To run the project locally:

  ```bash
  python app.local.py

  # Open localhost:5000
  ```

## Directory Structure

  ```bash
  .
  ├── static              # Contains static files like images,css,js,videos etc. - will be pushed to s3 eventually
  ├── template            # Contains all the templates - use `{{ url_for('static', filename='path/to/file') }}` for s3 links to work
  ├── app.py              # Contains all the routing stuffs
  ├── app.local.py        # To run project locally before deployment
  ├── upload-to-s3.py     # Python script to upload content from static folder to s3 bucket - run it before deployment
  ├── requirements.txt    # Python packages list - to recreate when new packages are installed, do "pip freeze > requirements.txt"
  ```

## Deploying

1. Add all your api-endpoints, static files and templates.

1. Run `upload-to-s3.py` script to upload all your static files to s3.

```bash
  python3 upload-to-s3.py
```

1. Install ZAPPA. If you ran `pip install -r requirements.txt` before, you should have zappa installed. Otherwise, install using `pip install zappa`

1. Run `zappa init` and provide the values as required for the configuration.

1. Once configured, you'll see a `zappa_settings.json` file.

1. Now, run `zappa deploy` to deploy your website. After successful deployment, You'll get an endpoint which you can use to visit your website.

Yayyy! Your site is live.