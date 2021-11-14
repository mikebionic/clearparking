# -*- coding: utf-8 -*-

import decimal

units = (
	u'nol',
	(u'bir', u'bir'),
	(u'iki', u'iki'),
	u'üç', u'dört', u'bäş',
	u'alty', u'ýedi', u'sekiz', u'dokuz'
)

teens = (
	u'on', u'on bir',
	u'on iki', u'on üç',
	u'on dört', u'on bäş',
	u'on alty', u'on ýedi',
	u'on sekiz', u'on dokuz'
)

tens = (
	teens,
	u'ýigrimi', u'otuz',
	u'kyrk', u'elli',
	u'altmyş', u'ýetmiş',
	u'segsen', u'togsan'
)

hundreds = (
	u'ýüz', u'iki ýüz',
	u'üç ýüz', u'dört ýüz',
	u'bäş ýüz', u'alty ýüz',
	u'ýedi ýüz', u'sekiz ýüz',
	u'dokuz ýüz'
)

orders = (
	((u'müň', u'müň', u'müň'), 'm'),
	((u'million', u'million', u'million'), 'm'),
	((u'milliard', u'milliard', u'milliard'), 'm'),
	((u'kwadrillion', u'kwadrillion', u'kwadrillion'), 'm'),
	((u'kwintillion', u'kwintillion', u'kwintillion'), 'm'),
	((u'sekstillion', u'sekstillion', u'sekstillion'), 'm'),
	((u'septillion', u'septillion', u'septillion'), 'm'),
	((u'oktillion', u'oktillion', u'oktillion'), 'm'),
	((u'nonillion', u'nonillion', u'nonillion'), 'm'),
	((u'desillion', u'desillion', u'desillion'), 'm'),
	((u'undesillion', u'undesillion', u'undesillion'), 'm'),
	((u'duodesillion', u'duodesillion', u'duodesillion'), 'm'),
	((u'tredesillion', u'tredesillion', u'tredesillion'), 'm'),
	((u'kwattordesillion', u'kwattordesillion', u'kwattordesillion'), 'm'),
	((u'kwindesillion', u'kwindesillion', u'kwindesillion'), 'm'),
	((u'sexdesillion', u'sexdesillion', u'sexdesillion'), 'm'),
	((u'septendesillion', u'septendesillion', u'septendesillion'), 'm'),
	((u'oktodesillion', u'oktodesillion', u'oktodesillion'), 'm'),
	((u'nowemdesillion', u'nowemdesillion', u'nowemdesillion'), 'm'),
	((u'wingitillion', u'wingitillion', u'wingitillion'), 'm'),
)


minus = u'minus'


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