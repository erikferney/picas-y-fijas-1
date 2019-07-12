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

def GenerarLista(tam):
	lista = []

	while len(lista) < tam:
		num = randint(0,10)

		if not num in lista:
			lista.append(num)

	return lista

listaOrig = GenerarLista(3)
print listaOrig

#FUNCIÓN RECURSIVA QUE EXIGE AL USUARIO QUE LA CADENA SEA
#DE 3 DIGITOS, DE LO CONTRARIO LA VA A PEDIR UNA Y OTRA VEZ
def valCadena():
	lStIngr = raw_input("Ingrese una cifra de tres digitos: ")
	
	if len(lStIngr) <> 3:
		print "No ha ingresado una cadena de 3 digitos"
		return valCadena()
	
	return lStIngr

for i in range(5):
	lStCifra = valCadena()
		
	indice = 0
	picas = 0
	fijas = 0

	digito = [int(x) for x in list(lStCifra)]		
	
	picas = countPicas(listaOrig, digito)
	fijas = countFijas(listaOrig, digito)
	
	gLsIntentos.append([lStCifra, "Picas: " + str(picas), "Fijas: " + str(fijas)])

for iMatriz in gLsIntentos:
	lStResumen = "Con el valor: "
	for iLista in range(len(iMatriz)):		
		lStResumen = lStResumen + str(iMatriz[iLista])
		
		if iLista == 0:
			lStResumen = lStResumen + ", usted obtuvo:"
		
		lStResumen = lStResumen + " "
	
	print lStResumen