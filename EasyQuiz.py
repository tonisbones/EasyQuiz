import json
import os
from flask import Flask, render_template, url_for
app = Flask(__name__)

header = """
    <!DOCTYPE html>
    <html>
    <head></head>
    <body>
"""
footer = """
    </body>
    </html>
"""
def readJson(filename):
    with open(filename, "r") as f:
        return json.loads(f.read())
    return None
@app.route("/")
def index():
	return render_template('index.html')
"""
this will be a page to test out the 
layout of a newly created json file
"""
#still not working quite right
@app.route("/jsontest/<jsonFile>")
def jsontest(jsonFile):
    jdict = readJson(os.path.join(os.getcwd(), "static/%s.json" % jsonFile))
    return "works"
    #return jdict["returnEmail"]
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
        return 'User %s' % username
if __name__ == "__main__":
	app.run()
