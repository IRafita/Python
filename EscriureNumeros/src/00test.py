def ViVoToViIExample (File):
	Vdd = 5.01
	f = open ('ViI', 'w')
	for line in open (File):
		x, y = line[:-1].split ('\t')
		y = Vdd -float(y)
		f.write (x + '\t' + str(y) + '\n')
	f.close ()

def ReadingFile ():
	o = []
	l = []
	for line in open ('conversor.Sdata', 'r'):
		print (line)
		if line[0] == '\\':
			o += [[line[:-1]] + l]
			l = []
		else:
			l += [line[:-1]]
	o += l
	return o

"""
Aqui la idea era d'agafar el fitxer i generar-ho
A causa d'un baix nivell de transformar-ho amb lletres correctament, ho fare amb el codi directament

Si admeto que per aqui, ara per ara no se com fer-ho
"""
