from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
	return "iam balaji-gv from scb chennai"

@app.route("/phone")
def lwphone():
	return "9949095520"

app.run(host="0.0.0.0")
