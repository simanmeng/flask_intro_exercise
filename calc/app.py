# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def app_add():
    """add a & b parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = add(a,b)
    return str(res)

@app.route('/sub')
def app_sub():
    """subtract a & b parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = sub(a,b)
    return str(res)

@app.route('/mult')
def app_mult():
    """multiply a & b parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = mult(a,b)
    return str(res)

@app.route('/div')
def app_div():
    """divide a & b parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = div(a,b)
    return str(res)

OPERATORS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operator>')
def math_operator(operator):
    """Handles math operation of a & b parameters based on input operator"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    res = OPERATORS[operator](a, b)
    return str(res)


