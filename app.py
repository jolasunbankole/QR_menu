from flask import Flask, jsonify, request

app = Flask(__name__)

#use index page as a landing page that uses phone camera to scan QR code and then redirect to menu page
@app.route("/Order")
def index():
    return 'Index Page'

@app.route('/Menu')
def menu():
    return 'Menu'




