from flask import Flask, render_template, request, jsonify
from db import tasks
# from flask import render


app = Flask(__name__)


@app.route("/api", methods=['GET'])
def index():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True, host='localhost')