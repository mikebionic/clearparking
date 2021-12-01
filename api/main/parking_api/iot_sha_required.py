# -*- coding: utf-8 -*-
from flask import jsonify, request
from functools import wraps

from main.config import Config

def get_bearer_from_header(auth_header):
	auth_token = None

	try:
		auth_header.split(" ")[0].lower().index("bearer")
		auth_token = auth_header.split(" ")[1]
	except:
		pass
	return auth_token


def iot_sha_required(f):
	@wraps(f)
	def decorated(*args,**kwargs):
		auth_token = None

		auth_token = get_bearer_from_header(request.headers.get('Authorization'))
		if not auth_token and 'x-access-token' in request.headers:
			auth_token = request.headers['x-access-token']

		if not auth_token:
			return jsonify({"message": "Token is missing!"}), 401

		if auth_token != Config.IOT_SYNCH_SHA:
			return jsonify({"message": "Token is invalid!"}), 401

		return f(*args,**kwargs)

	return decorated