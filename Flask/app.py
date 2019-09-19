from flask import Flask, request, json, jsonify
import requests
app = Flask(__name__)


@app.route('/add',methods=['POST'])
def add():
    numbers = request.get_json()
    sum = numbers['First'] + numbers['Second']
    dict = {
        'sum': sum
    }
    return jsonify(dict)


if __name__ == '__main__':
    app.run()
