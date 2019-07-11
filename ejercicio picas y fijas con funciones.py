#import random
from random import randint
#import random as rn

gLsIntentos = []

def countPicas(lsOrig, lsUsua):
	conteo = 0
	for num in range(len(lsUsua)):
		if lsUsua[num] in lsOrig and lsUsua[num] <> lsOrig[num]:
			conteo += 1
	
	return conteo

def countFijas(lsOrig, lsUsua):
	conteo = 0
	for num in range(len(lsUsua)):
	#for num in lsUsua:
		if lsUsua[num] == lsOrig[num]:
			conteo += 1
	
	return conteo

def GenerarLista():
	lista = []

	while len(lista) < 3:
		num = randint(0,9)

		if not num in lista:
			lista.append(num)

	return lista

listaOrig = GenerarLista()
print listaOrig

def valCadena(cadena):
	

a=raw_input("Prueba tu suerte, ingresa un valor de no mas de tres caracteres: ")
listaUsua = [int(x) for x in list(a)]

print "fijas " + str(countFijas(listaOrig, listaUsua))
print "picas " + str(countPicas(listaOrig, listaUsua))

for i in range(5):
	a=raw_input("Prueba tu suerte, ingresa un valor de no mas de tres caracteres: ")
	
	if len(a) <> 3:
		print "La longitud maxima de la cadena es de tres digitos"
		break
		
	indice = 0
	picas = 0
	fijas = 0

	for lt in range(len(a)):
		if lista[lt]==int(a[lt]):
			fijas += 1
		elif int(a[lt]) in lista:
			picas += 1
	#for letra in a:
	#	if lista[indice]==int(letra):
	#		fijas += 1
	#	elif int(letra) in lista:
	#		picas += 1
	#       indice += 1

	##while indice < len(a):
                #if lista[indice]==int(a[indice]):
		#	fijas += 1
		#elif int(a[indice]) in lista:
		#	picas += 1
		
	
	if fijas == len(a):
		print "Felicidades, has obtenido todas las fijas"
		break
	else:
		print "Obtuviste " + str(fijas) + " fijas y " + str(picas) + " picas"
"""