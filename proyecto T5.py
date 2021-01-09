import re
#patron = re.compile('a[3-5]+')# coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
#print( input("Introduce un texto") );
archivo=open('datosP.txt','r')
#print("el texto es: "+archivo.read())
mensaje=archivo.read()

var=0
	#sentencia de asignacion
patron = re.compile('([A-Za-z]+\w?\=[A-Za-z0-9]+\w?\s)')
print (patron.findall(mensaje))
if patron.findall(mensaje)!=[]:
	print("falto punto y coma")
else:
	var=var+1
patron2 = re.compile('[0-9]+\w?\=[A-Za-z0-9]+\w?\;')
print (patron2.findall(mensaje))
if patron2.findall(mensaje)!=[]:
	print("no puede dar valor a una variable que empieza o es un numero")
else:
	var=var+1
patron3 = re.compile('([A-Za-z]+\w?\=\-?([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?)(\+|\-|\*|\/)\(([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?)((\+|\-|\*|\/)([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?))?\;)')
print (patron3.findall(mensaje))
if patron3.findall(mensaje)!=[]:
	print("te falta el parentesis derecho")
else:
	var=var+1
patron4 = re.compile('([A-Za-z]+\w?\=\-?([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?)(\+|\-|\*|\/)([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?)((\+|\-|\*|\/)([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?))?\)\;)')
print (patron4.findall(mensaje))
if patron4.findall(mensaje)!=[]:
	print("te falta el parentesis izquierdo")
else:
	var=var+1
patron5 = re.compile('(\d{1,7}(\.\d{1,7})?)(\<|\>|\=\=|\<\=|\>\=|\!\=)\-?([A-Za-z]+\w?|\d{1,7}(\.\d{1,7})?)')
print (patron5.findall(mensaje))
if patron5.findall(mensaje)!=[]:
	print("no puede comparar una variable que empieza o es un numero")
else:
	var=var+1
patron6 = re.compile('(\S\W\(([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?)(\<|\>|\=\=|\<\=|\>\=|\!\=)([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?)\)\{([+\n.\s\S]{0,9})\})')
print (patron6.findall(mensaje))
if patron6.findall(mensaje)!=[]:
	print("no se encontro la palabra reservada if")
else:
	var=var+1
patron7 = re.compile('(if([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?)(\<|\>|\=\=|\<\=|\>\=|\!\=)([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?)\)\{([+\n.\s\S]{0,9})\})')
print (patron7.findall(mensaje))
if patron7.findall(mensaje)!=[]:
	print("te falta el parentesis izquierdo")
else:
	var=var+1
patron8 = re.compile('(if\(([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?)(\<|\>|\=\=|\<\=|\>\=|\!\=)([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?)\{([+\n.\s\S]{0,9})\})')
print (patron8.findall(mensaje))
if patron8.findall(mensaje)!=[]:
	print("te falta el parentesis derecho")
else:
	var=var+1
if var==8:
	print(var)
	print("compilacion exitosa")
archivo.close()




