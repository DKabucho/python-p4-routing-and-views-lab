#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text
    
@app.route('/count/<int:number>')
def count(number):
    numbers = '\n'.join(str(i) for i in range(number + 1))
    return numbers, 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
