from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from app import app_code

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({'response': 'the server is working...',})


@cross_origin
@app.route('/binary_text', methods=['POST'])
def text_binary():
    data = request.json
    text = app_code(data)
    return text


if __name__ == '__main__':
    app.run(debug=True, port=4000)

