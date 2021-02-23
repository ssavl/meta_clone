from flask import Flask, render_template, request, jsonify
from db import BOOKS
from flask_cors import CORS

# configurations
DEBUG = True

# application
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# CORS(app, resources={r"/api": {"origins": "*"}})  # Даем любому ip делать cross-origin-requests TODO: надо изменить!



@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })












if __name__ == '__main__':
    app.run(debug=True, host='localhost')