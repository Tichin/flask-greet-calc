from flask import Flask
from flask import request
import operations

app = Flask(__name__)

@app.get('/add')
def add():
    '''adds the two parameters together and returns them'''
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
    except ValueError:
        return "Both parameters must be numbers"
    result = operations.add(a, b)
    return f"{result}"

@app.get('/sub')
def sub():
    '''subtracts the two parameters and returns result'''
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
    except ValueError:
        return "Both parameters must be numbers"
    result = operations.sub(a, b)
    return f"{result}"

@app.get('/mult')
def mult():
    '''multiplies the two parameters and returns result'''
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
    except ValueError:
        return "Both parameters must be numbers"
    result = operations.mult(a, b)
    return f"{result}"

@app.get('/div')
def div():
    '''divides the two parameters and returns result'''
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
    except ValueError:
        return "Both parameters must be numbers"
    try:
        result = operations.div(a, b)
    except ZeroDivisionError:
        # they tried to divide by 0
        return "Second argument cannot be 0"
    return f"{result}"



