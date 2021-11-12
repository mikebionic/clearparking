import sys
import redis
import json
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath('.')
load_dotenv(path.join(basedir, '.env'))

class Config:
	OS_TYPE = sys.platform
	APP_BASEDIR = path.abspath('.')

	SECRET_KEY = environ.get('SECRET_KEY')
	APP_PORT = int(environ.get('APP_PORT')) if environ.get('APP_PORT') else 5000
	APP_HOST = environ.get('APP_HOST') or "0.0.0.0"

	DEVICE_SECRET = environ.get('SECRET_KEY') or "secret_pass_key"

	DB_TYPE = environ.get('DB_TYPE') or 'postgres'
	DB_URI_DATA = {
		'user': environ.get('DB_USERNAME'),
		'pw': environ.get('DB_PASSWORD'),
		'db': environ.get('DB_DATABASE'),
		'host': environ.get('DB_HOST'),
		'port': environ.get('DB_PORT'),
		'driver': environ.get('DB_DRIVER') or '',
		'additionalFields': environ.get('DB_ADDITIONAL_FIELDS') or ''
	}
	if DB_TYPE.lower() == "mssql":
		SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s?driver=%(driver)s%(additionalFields)s" % DB_URI_DATA

	if DB_TYPE.lower() == "postgres":
		SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s%(additionalFields)s' % DB_URI_DATA
	
	SQLALCHEMY_ECHO = int(environ.get('SQLALCHEMY_ECHO')) if environ.get('SQLALCHEMY_ECHO') else 0
	API_URL_PREFIX = environ.get('API_URL_PREFIX') or '/api'

	ADMIN_USERNAME = "admin"
	ADMIN_PIN = "123"