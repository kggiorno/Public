import oauth2
import urllib.parse as urlparse

import settings

consumer = oauth2.Consumer(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)

def get_request_token():
		client = oauth2.Client(consumer)

		response, content = client.request(settings.REQUEST_TOKEN_URL, 'POST')
		if response.status != 200:
			print("An error occurred during request token retrieval attempt.")

		return dict(urlparse.parse_qsl(content.decode('utf-8')))

def get_oauth_verifier(request_token):
	print("Navigate to the following site to retrieve the authorization pin:")
	print("{}?oauth_token={}".format(settings.AUTHORIZATION_URL, request_token['oauth_token']))

	return input("Enter the authorization pin: ")

def get_access_token(request_token, oauth_verifier):
	token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
	token.set_verifier(oauth_verifier)

	client = oauth2.Client(consumer, token)

	response, content = client.request(settings.ACCESS_TOKEN_URL, 'POST')
	return dict(urlparse.parse_qsl(content.decode('utf-8')))