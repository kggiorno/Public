from flask import Flask, render_template, session, redirect
from twitter_utilities import get_request_token

app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def homepage():
	return render_template('home.html')

@app.route('/login/twitter')
def twitterLogin():
	request_token = get_request_token()
	session['request_token'] = request_token

	return redirect('http://example.com')


app.run(port=5000)
