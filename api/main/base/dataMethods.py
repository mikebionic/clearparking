import base64
from datetime import datetime
from decimal import Decimal


def configureDecimal(value):
	try:
		value = Decimal(value).quantize(Decimal('0.01'))
	except Exception as ex:
		pass
	return value


def configureFloat(value):
	try:
		value = float(value)
	except Exception as ex:
		value = 0
	return value


def boolCheck(value):
	if value == 'False' or value == 'false' or value == '0' or value == 0:
		value = False
	elif value:
		value = True
	else:
		value = False
	return value


def dateDataCheck(date):
	try:
		print(date)
		date = datetime.strptime(date, "%Y-%m-%d")
	except Exception as ex:
		date = None
	print(date)
	return date


def apiDataFormat(date):
	try:
		date = date.strftime("%Y-%m-%d %H:%M:%S")
	except Exception as ex:
		date = None
	return date


def apiCheckImageByte(image):
	try:
		image = base64.encodebytes(image).decode('ascii'),
	except Exception as ex:
		image = None

	return image


def configureNulls(data):
	for e in data:
		if data[e] == '' or data[e] == 0:
			data[e] = None
	return data


def configureEmptyQuotesNulls(data):
	for e in data:
		if data[e] == '':
			data[e] = None
	return data


def prepare_data(dropdown,page,title):
	template_data = {
		'dropdown': dropdown,
		'page': page,
		'title': title,
	}
	return template_data