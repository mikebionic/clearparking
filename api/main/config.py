import sys
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath('.')
load_dotenv(path.join(basedir, '.env'))

class Config:
	OS_TYPE = sys.platform
	APP_BASEDIR = path.abspath('.')

	SECRET_KEY = environ.get('SECRET_KEY')

	# This is for flutter or other frontend
	IOT_SYNCH_SHA = environ.get('IOT_SYNCH_SHA')
	APP_PORT = int(environ.get('APP_PORT')) if environ.get('APP_PORT') else 5000
	APP_HOST = environ.get('APP_HOST') or "0.0.0.0"

	DB_STRUCTURE = environ.get('DB_STRUCTURE') or 'saphasap'
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

	# This is for device itself
	IOT_DEVICE_URL = environ.get('IOT_DEVICE_URL') or "http://192.168.1.100"
	IOT_DEVICE_KEY = environ.get('IOT_DEVICE_KEY') or "secret_key"

	ADMIN_USERNAME = "admin"
	ADMIN_PIN = "123"
	IOT_RESOURCE_GUID = environ.get('IOT_RESOURCE_GUID')
	REG_NUM_RANDOM_RANGE = int(environ.get('REG_NUM_RANDOM_RANGE')) if environ.get('REG_NUM_RANDOM_RANGE') else 9999999
	SIMULATE_REQUEST = int(environ.get('SIMULATE_REQUEST')) if environ.get('SIMULATE_REQUEST') else 1

	USE_SERIAL_DEVICE = int(environ.get('USE_SERIAL_DEVICE')) if environ.get('USE_SERIAL_DEVICE') else 1
	SERIAL_DEVICE_CONTROL_APP_PATH = environ.get('SERIAL_DEVICE_CONTROL_APP_PATH') or 'bin/app'
	SERIAL_BAUDRATE = int(environ.get('SERIAL_BAUDRATE')) if environ.get('SERIAL_BAUDRATE') else 115200
	SERIAL_PORT = environ.get('SERIAL_PORT') or "/dev/ttyUSB0"
	SERIAL_DEVICE_APP_EXECUTION_COMMAND = f"{path.join(basedir, SERIAL_DEVICE_CONTROL_APP_PATH)} -b={SERIAL_BAUDRATE} -p={SERIAL_PORT}"