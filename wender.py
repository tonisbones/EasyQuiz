from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World, I'm Testing!!"
if __name__ == "__main__":
	app.run()
