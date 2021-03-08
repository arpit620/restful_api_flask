from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


# Basic hello world - returns text
@app.route('/')
def hello_world():
    return "Hello World..!!"


# Return sample json file
@app.route('/simple')
def simple():
    return jsonify(message="Hello from simple function...!!!")


# Return sample json file , followed by return status code
@app.route('/not_found')
def not_found():
    return jsonify(message="Not Found"), 404


# Send parameters via url
# Endpoint: http://localhost:5000/parameters?name=Bruce&age=28
@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough."), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old enough!")


# Used for cleaner urls
# Endpoint: http://localhost:5000/url_variables/bruce/20
# Default datatype is string. Can specify explicitly
@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough."), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old enough!")


if __name__ == '__main__':
    app.run()

