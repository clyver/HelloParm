from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/recipe', methods=["POST", "GET"])
def recipe():
	return "test"
