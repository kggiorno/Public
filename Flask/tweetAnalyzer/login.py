import oauth2
import urllib.parse as urlparse

from user import User
from database import Database
import settings
import twitter_utilities

# Initialize DB
Database.initialize(user='postgres', password='admin', host='localhost', database='learning')

#Check for user in DB, if doesn't exist, prompt user to create user/oauthtoken
user_email = input("Enter your e-mail address: ")
user = User.load_from_db_by_email(user_email)
if user:
	pass
else:
	request_token = twitter_utilities.get_request_token()
	oauth_verifier = twitter_utilities.get_oauth_verifier(request_token)
	access_token = twitter_utilities.get_access_token(request_token, oauth_verifier)

	first_name = input("Enter your first name: ")
	last_name = input("Enter your last name: ")

	user = User(user_email, first_name, last_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)
	user.save_to_db()

tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images')

for tweet in tweets['statuses']:
	print(tweet['text'])
