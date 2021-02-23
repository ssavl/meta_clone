from flask import Flask, render_template, request, jsonify
from db import tasks
from flask_cors import CORS

# configurations
DEBUG = True

# application
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/api": {"origins": "*"}})  # Даем любому ip делать cross-origin-requests TODO: надо изменить!




@app.route("/api", methods=['GET', 'POST'])
def index():
    return jsonify({'tasks': tasks})













if __name__ == '__main__':
    app.run(debug=True, host='localhost')