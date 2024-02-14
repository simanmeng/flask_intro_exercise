from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Show Welcome"""
    return "Welcome!"

@app.route('/welcome/home')
def welcome_home():
    """Show welcome home"""
    return "Welcome home"

@app.route('/welcome/back')
def welcome_back():
    """Show welcome back"""
    return "Welcome back"
