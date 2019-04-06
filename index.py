from flask import Flask
import time
print("new program")

app = Flask(__name__)
@app.route('/')
def index():
	return'<h1>Deployed to Heroku</h1>'