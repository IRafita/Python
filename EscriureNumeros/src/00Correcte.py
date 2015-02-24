"""
farem un intent de catala correcte, accents i etc
"""

def mt ():
	for j in range (10):
		for i in range (10):
			print (decenes (j, i))

# Fa referencia a que aqui el zero s'escriu, ja que no interesa sempre
def unitatsUniques (e):
	return {1:'un',
		2:'dos',
		3:'tres',
		4:'quatre',
		5:'cinc',
		6:'sis',
		7:'set',
		8:'vuit',
		9:'nou',
		0:'zero'}[e]
def unitats (e):
	return {1:'un',
		2:'dos',
		3:'tres',
		4:'quatre',
		5:'cinc',
		6:'sis',
		7:'set',
		8:'vuit',
		9:'nou',
		0:''}[e]

# prou important que retorni null quan entra 0, 0
def decenes (d, u):
	if d == 0: return unitats (u)
	elif d == 1:
		if u > 0:
			if u > 6:
				return 'di' + unitats (u)
			return {1:'on',
				2:'dot',
				3:'tret',
				4:'cator',
				5:'quin',
				6:'set'}[u] + 'ze'
		return 'deu'
	elif d == 2:
		if u == 0: return 'vint'
		return 'vint-i-' + unitats (u)
	else:
		s = unitats (u)
		if s: s = '-' + s
		return {3:'tre',
			4:'quara',
			5:'cinqua',
			6:'seixa',
			7:'seta',
			8:'vuita',
			9:'nora'}[d] + 'nta' + s

def centenar (c, d, u):
	if c == 0: return decenes (d, u)
	if c == 1: return	'cent '		+ decenes (d, u)
	return unitats (c) +	'-cents '	+ decenes (d, u)

def mil (c1, d1, u1, c, d, u):
	if c1 == d1 == u1 == 0: return centenar (c, d, u)
	if c1 == d1 == 0 and u1 == 1: return 'mil ' + centenar (c, d, u)
	return centenar (c1, d1, u1) + ' mil ' + centenar (c, d, u)

def milio (c2, d2, u2, c1, d1, u1, c, d, u):
	if c2 == d2 == u2 == 0: return mil (c1, d1, u1, c, d, u)
	if c2 == d2 == 0 and u2 == 1: return 'un milió ' + mil (c1, d1, u1, c, d, u)
	return centenar (c2, d2, u2) + ' milions ' + mil (c1, d1, u1, c, d, u)

def miliard (c3, d3, u3, c2, d2, u2, c1, d1, u1, c, d, u):
	if c3 == d3 == u3 == 0: return milio (c2, d2, u2, c1, d1, u1, c, d, u)
	if c3 == d3 == 0 and u3 == 1: return 'un miliard ' + milio (c2, d2, u2, c1, d1, u1, c, d, u)
	return centenar (c3, d3, u3) + ' miliards ' + milio (c2, d2, u2, c1, d1, u1, c, d, u)

def bilio (c5, d5, u5, c4, d4, u4, c3, d3, u3, c2, d2, u2, c1, d1, u1, c, d, u):
	if c5 == d5 == u5 == c4 == d4 == u4 == 0: return miliard (c3, d3, u3, c2, d2, u2, c1, d1, u1, c, d, u)
	if c5 == d5 == u5 == c4 == d4 == 0 and u4 == 1: return 'un bilió ' + miliard (c3, d3, u3, c2, d2, u2, c1, d1, u1, c, d, u)
	return mil (c5, d5, u5, c4, d4, u4) + ' bilions ' + miliard (c3, d3, u3, c2, d2, u2, c1, d1, u1, c, d, u)

"""
He detectat contradiccions... Aixi que no se si realment la cosa es tal i com puc arribar a pensar jo
"""

def parser ():
	x = input("Enter a number: ")
	o = [0] * 18
	for i in range (len (x)):
		o[i] = int (x[-1 -i])
	return (bilio (o[17], o[16], o[15], o[14], o[13], o[12], o[11], o[10], o[9], o[8], o[7], o[6], o[5], o[4], o[3], o[2], o[1], o[0]))
