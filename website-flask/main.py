"""
Didn't finish the part, cuz it use Heroku as the Cloud application which I think I won't use it in the future.
89: Creating a Python Virtual Environment
90: Deploying the Website to a Live Server
91: Maintaining the Website
"""

# pip install flask

from flask import Flask, render_template

# __name__ get this file name
app = Flask(__name__)

# Rute url to the function that next to it. In this case visit / will all sai_home()
@app.route('/')
def sai_home():
	return render_template("home.html")

@app.route('/about')
def about():
	# return "This a about page"
	return render_template("about.html")

if __name__ == "__main__":
	app.run(debug=True)