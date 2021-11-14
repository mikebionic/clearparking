# -*- coding: utf-8 -*-

import decimal

units = (
	'zero',
	('one','one'),
	('two','two'),
	'three','four','five',
	'six','seven','eight','nine'
)

teens = (
	'ten','eleven',
	'twelve','thirteen',
	'fourteen','fifteen',
	'sixteen','seventeen',
	'eighteen','nineteen'
)

tens = (
	teens,
	'twenty','thirty',
	'forty','fifty',
	'sixty','seventy',
	'eighty','ninety'
)

hundreds = (
	'hundred','two hundred',
	'three hundred','four hundred',
	'five hundred','six hundred',
	'seven hundred','eight hundred',
	'nine hundred'
)

orders = (
	(('thousand','thousand','thousand'),'m'),
	(('million','million','million'),'m'),
	(('billion','billion','billion'),'m'),
	(('quadrillion','quadrillion','quadrillion'),'m'),
	(('quintillion','quintillion','quintillion'),'m'),
	(('sextillion','sextillion','sextillion'),'m'),
	(('septillion','septillion','septillion'),'m'),
	(('octillion','octillion','octillion'),'m'),
	(('nonillion','nonillion','nonillion'),'m'),
	(('decillion','decillion','decillion'),'m'),
	(('undecillion','undecillion','undecillion'),'m'),
	(('duodecillion','duodecillion','duodecillion'),'m'),
	(('tredecillion','tredecillion','tredecillion'),'m'),
	(('quattuordecillion','quattuordecillion','quattuordecillion'),'m'),
	(('quindecillion','quindecillion','quindecillion'),'m'),
	(('sexdecillion','sexdecillion','sexdecillion'),'m'),
	(('septendecillion','septendecillion','septendecillion'),'m'),
	(('octodecillion','octodecillion','octodecillion'),'m'),
	(('novemdecillion','novemdecillion','novemdecillion'),'m'),
	(('vigintillion','vigintillion','vigintillion'),'m'),
)

minus = 'minus'

def thousand(rest, sex):
	prev = 0
	plural = 2
	name = []
	use_teens = rest % 100 >= 10 and rest % 100 <= 19
	if not use_teens:
		data = ((units, 10), (tens, 100), (hundreds, 1000))
	else:
		data = ((teens, 10), (hundreds, 1000))
	for names, x in data:
		cur = int(((rest - prev) % x) * 10 / x)
		prev = rest % x
		if x == 10 and use_teens:
			plural = 2
			name.append(teens[cur])
		elif cur == 0:
			continue
		elif x == 10:
			name_ = names[cur]
			if isinstance(name_, tuple):
				name_ = name_[0 if sex == 'm' else 1]
			name.append(name_)
			if cur >= 2 and cur <= 4:
				plural = 1
			elif cur == 1:
				plural = 0
			else:
				plural = 2
		else:
			name.append(names[cur-1])
	return plural, name


def num2text(num, main_units=((u'', u'', u''), 'm')):
	_orders = (main_units,) + orders
	if num == 0:
		return ' '.join((units[0], _orders[0][0][2])).strip() # ноль
	rest = abs(num)
	ord = 0
	name = []
	while rest > 0:
		plural, nme = thousand(rest % 1000, _orders[ord][1])
		if nme or ord == 0:
			name.append(_orders[ord][0][plural])
		name += nme
		rest = int(rest / 1000)
		ord += 1
	if num < 0:
		name.append(minus)
	name.reverse()
	return ' '.join(name).strip()

def decimal2text(value, places=2,
				 int_units=(('', '', ''), 'm'),
				 exp_units=(('', '', ''), 'm')):
	value = decimal.Decimal(value)
	q = decimal.Decimal(10) ** -places

	integral, exp = str(value.quantize(q)).split('.')
	return u'{} {}'.format(
		num2text(int(integral), int_units),
		num2text(int(exp), exp_units))