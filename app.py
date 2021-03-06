from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
import os

if (os.environ['FLASK_ENV']=='production'):
    app = Flask(__name__, static_folder='my-app/build', static_url_path='')
else:
    app = Flask(__name__)


CORS(app)

@app.route('/api', methods=['GET'])
@cross_origin()
def index():
    return {
        "tutorial": f"Flask React Heroku (env:{os.environ['FLASK_ENV']})"
    }

@app.route('/')
def serve():
    if (os.environ['FLASK_ENV']=='production'):
        return send_from_directory(app.static_folder, 'index.html')
    else:
        return {"TEE LOG says: ": f"I'm alive!!! Running in ({os.environ['FLASK_ENV']})"}

if __name__ == '__main__':
    app.run()