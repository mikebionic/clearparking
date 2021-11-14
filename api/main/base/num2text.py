# -*- coding: utf-8 -*-
from .en_num2text import num2text as en_num2text
from .ru_num2text import num2text as ru_num2text
from .tk_num2text import num2text as tk_num2text

from .ru_num2text import decimal2text as ru_decimal2text
from .tk_num2text import decimal2text as tk_decimal2text
from .en_num2text import decimal2text as en_decimal2text

import decimal

def num2text(num, language='en'):
	try:
		if language=='en':
			result = en_num2text(num)
		elif language=='ru':
			result = ru_num2text(num)
		elif language=='tk':
			result = tk_num2text(num)
		else:
			result = en_num2text(num)
	except Exception as ex:
		print(ex)
		result = "out of range"

	return result

def price2text(num, language='en', currencyCode='TMT'):
	currencyCodesDict = {
		'TMT': [
						{'en': ['manats', 'tenge']},
						{'ru': ['манат', 'копеек']},
						{'tk': ['manat', 'teňňe']},
					],
		'USD': [
						{'en': ['dollars', 'cents']},
						{'ru': ['долл.', 'центов']},
						{'tk': ['dollar', 'sent']},
					],
		'EUR': [
						{'en': ['pounds', 'coins']},
						{'ru': ['фунтов', 'копеек']},
						{'tk': ['funt', 'teňňe']},
					],
		'RUB': [
						{'en': ['rub', 'coins']},
						{'ru': ['рублей', 'копеек']},
						{'tk': ['rubl', 'teňňe']},
					],
	}

	try:
		for currency in currencyCodesDict:
			if currency == currencyCode:
				for languages in currencyCodesDict[currency]:
					for lang in languages:
						if lang == language:
							res = languages[lang]
	except Exception as ex:
		print(ex)
		res = ''

	try:
		if language == 'en':
			if '.' in str(num):
				result = en_decimal2text(
					decimal.Decimal(num),
					int_units=((res[0], res[0], res[0]), 'f'),
					exp_units=((res[1], res[1], res[1]), 'm'))
			else:
				result = en_num2text(
					int(num),
					main_units=((res[0], res[0], res[0]), 'f'))

		elif language == 'ru':
			if '.' in str(num):
				result = ru_decimal2text(
					decimal.Decimal(num),
					int_units=((res[0], res[0], res[0]), 'f'),
					exp_units=((res[1], res[1], res[1]), 'm'))
			else:
				result = ru_num2text(
					int(num),
					main_units=((res[0], res[0], res[0]), 'f'))

		elif language == 'tk':
			if '.' in str(num):
				result = tk_decimal2text(
					decimal.Decimal(num),
					int_units=((res[0], res[0], res[0]), 'm'),
					exp_units=((res[1], res[1], res[1]), 'm'))
			else:
				result = tk_num2text(
					int(num),
					main_units=((res[0], res[0], res[0]), 'm'))

	except Exception as ex:
		print(ex)
		result = "out of range"

	return result