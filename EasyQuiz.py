import json
import os
from flask import Flask, render_template
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
@app.route("/")
def index():
	return render_template('index.html')
"""
this will be a page to test out the 
layuot of a newly created json file
"""
@app.route("/jsontest/<jsonFile>")
def jsontest(jsonFile):
    #need to figure out how to access files static to read json
    """
    json_file = open(os.path.join(os.path.dirname(__file__),"sample.json"),'r')
    data = json.load(json_file)
    pprint(data)
    json_data.close()
    """
    return jsonFile
    #return " %s <p> Works </p> %s" % header, footer
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
        return 'User %s' % username
if __name__ == "__main__":
	app.run()
