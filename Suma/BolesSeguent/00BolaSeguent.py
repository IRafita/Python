"""
Petits canvis efectuats
Ara funciona sense digits, nomes amb lletres
Ara esta corregit els problemes que tenia amb els espais

Confiem que tot estigui correcte, la veritat he fet una comprovacio inferior a 300 elements...
	D'aquesta manera poc puc assegurar el bon funcionament del parser
"""
def mini (a = 200, b = 300):
	for i in range (a, b):
		print (parser (str(i)))
		
# La entrada ha de ser un string ex '1234007'
def parser (e):
	o, q, t = ['zero', 'zero', 'zero'], 1, 0
	for i in e[::-1]:
		o[t] = dicDigitLeter (i)
		t += 1
		q += 1
		if q > 3:
			o += ['zero', 'zero', 'zero']
			q = 1
	while o[-3:] == ['zero', 'zero', 'zero']: o = o[:-3]
#	pdb.set_trace ()
	t = len(o)/3
	#print (o)
	if t == 0: return 'zero'
	if t <= 1: return centenar (o)
	if t <= 2: return mil (o)
	if t <= 4: return milio (o)
	if t <= 6: return bilio (o)
	if t <= 8: return trilio(o)
	return 'No sabem ;)\n Numerals en catala\n Numeral prefix\nTot aixo i mes a la wikipedia'

def dicDigitLeter (e):
	return {'1':'un',
		'2':'dos',
		'3':'tres',
		'4':'quatre',
		'5':'cinc',
		'6':'sis',
		'7':'set',
		'8':'vuit',
		'9':'nou',
		'0':'zero'}[e]

# 10^0
def unitats (e):
	return {'un':'un',
		'dos':'dos',
		'tres':'tres',
		'quatre':'quatre',
		'cinc':'cinc',
		'sis':'sis',
		'set':'set',
		'vuit':'vuit',
		'nou':'nou',
		'zero':''}[e]

# 10^1
def decenes (e):
	if e[0] == e[1] == 'zero': return ''
	if e[1] == 'zero': return unitats (e[0])
	elif e[1] == 'un':
		if e[0] == 'zero': return 'deu'
		if e[0] in ['set', 'vuit', 'nou']: return 'di' + unitats (e[0])
		return {'un':'on',
			'dos':'dot',
			'tres':'tret',
			'quatre':'cator',
			'cinc':'quin',
			'sis':'set'}[e[0]] + 'ze'
	elif e[1] == 'dos':
		if e[0] == 'zero': return 'vint'
		return 'vint-i-' + unitats (e[0])
	else:
		s = unitats (e[0])
		if s: s = '-' + s
		return {'tres':'tre',
			'quatre':'quara',
			'cinc':'cinqua',
			'sis':'seixa',
			'set':'seta',
			'vuit':'vuita',
			'nou':'nora'}[e[1]] + 'nta' + s

# 10^2
def centenar (e):
	s, m = decenes (e[:2]), 'cent'
	if e[-1] == 'zero': return s
	if e[-1] == 'un':
		if s: return m + ' ' + s
		return m
	if s: return unitats (e[-1]) + '-' + m + 's ' + s
	return unitats (e[-1]) +'-' + m + 's'

# 10^3
def mil (e):
	s, m = centenar (e[:3]), 'mil'
	if e[-1] == e[-2] == e[-3] == 'zero': return s
	if e[-1] == e[-2] == 'zero' and e[-3] == 'un':
		if s: return m + ' ' + s
		return m
	if s: return centenar (e[-3:]) + ' ' + m + ' ' + s
	return centenar (e[-3:]) + ' ' + m

# 10^6
def milio (e):
	s = mil (e[:6])
	if e[-1] == e[-2] == e[-3] == e[-4] == e[-5] == e[-6] == 'zero': return s
	if e[-1] == e[-2] == e[-3] == e[-4] == e[-5] == 'zero' and e[-6] == 'un':
		if s: return 'un milió ' + s
		return 'un milió'
	if s: return mil (e[-6:]) + ' milions ' + s
	return mil (e[-6:]) + ' milions'

# 10^12
def bilio (e):
	s = milio (e[:12])
	if e[-1] == e[-2] == e[-3] == e[-4] == e[-5] == e[-6] == 'zero': return s
	if e[-1] == e[-2] == e[-3] == e[-4] == e[-5] == 'zero' and e[-6] == 'un':
		if s: return 'un bilió ' + s
		return 'un bilió'
	if s: return mil (e[-6:]) + ' bilions ' + s
	return mil (e[-6:]) + ' bilions'

# 10^18
def trilio (e):
	s = bilio (e[:18])
	if e[-1] == e[-2] == e[-3] == e[-4] == e[-5] == e[-6] == 'zero': return s
	if e[-1] == e[-2] == e[-3] == e[-4] == e[-5] == 'zero' and e[-6] == 'un':
		if s: return 'un trilió ' + s
		return 'un trilió'
	if s: return mil (e[-6:]) + ' trilions ' + s
	return mil (e[-6:]) + ' trilions'

import pdb
