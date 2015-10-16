#!/usr/bin/python

#importamos la libreria necesaria para usar arreglos
import numpy as np

#variables de nuestros arreglos globales
arr=""
arr2=[]
arr4=[]


#####################################################################
#																	#
#																	#
#																	#
#					FUNCION PARA LEER EL ARCHIVO					#
#																	#
#																	#
#																	#
#####################################################################

#recibe de parametro la ruta
def leer(route):
	global arr,arr2,arr4
	tex=""
	arr3=[]
	archivo=open(route,'r')#abrimos el archivo y lo preparamos para escribir en el
	texto=archivo.readline()#leemos el archivo
	while texto!="":
		arr+=lector(texto)
		texto = archivo.readline()
	archivo.close()#cerramos el archivo
	RLE()
	for ix in range(len(arr4)):
		#print "arr4 numeros"
		#print str(arr4[ix])
		numerito=str(arr4[ix])
		#print "arr2 letras"
		#print arr2[ix]
		arr3+=(arr2[ix]+"-"+numerito+",")
	#print arr3
	print "Donde deseas guardar el resultado"
	ru=raw_input()
	for tt in arr3:
		#tex+=tt
		if tt == '#':
			break
		else:
			tex+=tt
	out=open(ru,'w')#creamos un archivo nuevo y lo preparamos para escribir en el
	out.write(tex)#escribimos el texto codificado en el archivo
	out.close()#cerramos el archivo creado


#####################################################################
#																	#
#																	#
#																	#
#			FUNCION PARA SEPARAR LAS LINEAS EN PARABRAS				#
#																	#
#																	#
#																	#
#####################################################################

def lector(frase):
	palabras=frase
	tam=len(palabras) #Tamano de la cadena de texto
	cadena=""
	arreglo=palabras.split(" ")#Separa la cadena de texto en caracteres
	i=0
	for i in arreglo:
		num = i
		if num != "":#Elimina los espacios
			cadena=cadena+num #Se almacena los caracteres en un acumulador pero sin espacios
	return cadena #Retorna la cadena

#####################################################################
#																	#
#																	#
#																	#
#					FUNCION PARA CODIFICAR							#
#																	#
#																	#
#																	#
#####################################################################

def RLE():
	global arr,arr2,arr4
	tam = len(arr)
	arr2=np.zeros(tam, dtype=str)#Se define el tamano del arreglo
	cont=1
	aux=0
	arr4=np.zeros(tam, dtype=int)
	for i in range(len(arr)):
		a=arr[i]
		if i != (len(arr)-1):
			if a==arr[i+1]:
				cont=cont+1
			else:
				arr2[aux]=a
				#arr2[aux+1]=cont
				arr4[aux]=int(cont)
				aux=aux+1
				cont=1
		else:
			arr2[aux]=a
			#arr2[aux+1]=cont
			arr4[aux]=int(cont)
			aux=aux+1
			cont=1
			arr2[aux]='#'
			break
	x=0

#####################################################################
#																	#
#																	#
#																	#
#				FUNCION PARA DECODIFICAR EL ARCHIVO					#
#																	#
#																	#
#																	#
#####################################################################

def dec(rutita):#Se pasa la direccion del archivo
	uax=0
	k=0
	hh=0
	#letritas=[]
	#letritas=lectura(rutita)#se guarda la cadena de texto del archivo
	#tam = len(letritas)#Se obtiene el tamano de la cadena de texto del archivo
	ar=open(rutita,'r')
	valor=""
	veces=""
	palabra=""
	lin=ar.readline()
	while lin != "":
		comas=lin.split(',')
		#print comas
		lin=ar.readline()
		for kd in range(len(comas)):
			#print comas[kd]
			c=comas[kd]
			guion=c.split('-')
			ban=1
			for gs in range(len(guion)):
				#print "guion"
				#print guion[gs]
				g=guion[gs]
				if ban==1:
					valor+=g
					ban=0
				else:
					veces+=(g+"+")
					#print veces
	#print "letras"
	#print valor
	#print"numeros"
	#print veces
	#print "split veces"
	nrep=veces.split('+')
	#print nrep
	c=0
	for l in valor:
		inrep=int(nrep[c])
		#print inrep
		wow=1
		while wow <= inrep:
			palabra+=l
			wow+=1
		c+=1
	#print palabra
	print "Donde deseas guardar tu archivo comprimido"
	ruta=raw_input()
	outfile=open(ruta,'w')#creamos un archivo nuevo y lo preparamos para escribir en el
	outfile.write(palabra)#escribimos el texto codificado en el archivo
	outfile.close()#cerramos el archivo creado

#####################################################################
#																	#
#																	#
#																	#
#				AQUI INICIA PPM COMPRIMIR							#
#																	#
#																	#
#																	#
#####################################################################

#aqui inicia ppm cifra
arrppm=[]
arrppm2=[]

def leerppm(r):
	archivo=open(r,'r')
	texto=archivo.readline()
	cont=0
	aux=0
	while texto!="":
		
		if cont==0 and texto[0]!='#':
			#print("Formato "+texto)
			form=texto
			cont=cont+1
			texto=archivo.readline()

		if cont==1 and texto[0]!='#':
			text=texto.split(" ")
			#print("Col "+text[0])
			#print("Filas "+text[1])
			fil = int(text[1])
			col = int(text[0])
			tam=fil*col*3
			creaArreglo(tam)
			cont=cont+1
			texto=archivo.readline()
		
		if cont==2 and texto[0]!='#':
			#print("Max "+texto)
			maxi= texto
			cont=cont+1
			texto=archivo.readline()
		
		if texto[0]!='#' and cont>2:
			#print("linea: "+texto)
			text=texto.split(" ")
			#print(text)
			for i in text:
				if i !="":
					#print(i)
					dato=int(i)
					llenaMatriz(dato,aux)
					aux=aux+1
		texto=archivo.readline()
	archivo.close()
	RLEppm()
	hacerPpm(form,fil,col,maxi)

def creaArreglo(tam):
	global arrppm, arrppm2
	#arr=np.arange(tam)
	arrppm=np.zeros(tam, dtype=int)
	arrppm2=np.zeros(tam, dtype=int)
	#print(arr)

def llenaMatriz(dato, indice):
	arrppm[indice]=dato;	

def RLEppm():
	global arrppm,arrppm2
	cont=1
	aux=0
	for i in range(len(arrppm)):
		a=arrppm[i]
		
		if i != (len(arrppm)-1):
			if a==arrppm[i+1]:
				cont=cont+1
			else:
				arrppm2[aux]=a
				arrppm2[aux+1]=cont
				aux=aux+2
				cont=1
		else:
			arrppm2[aux]=a
			arrppm2[aux+1]=cont
			aux=aux+2
			cont=1
			arrppm2[aux]=-1
			
	
def hacerPpm(form,f,c,m):
	global arrppm2
	print("Ingresa el nombre del nuevo archivo PPM: ")
	r = raw_input()
	archivo=open(r,'w')
	archivo.write(form)
	archivo.write(str(f)+" "+str(c)+"\n")
	archivo.write(m)
	for i in arrppm2:
		if(i!=-1):
			archivo.write(str(i)+" ")
		else:
			break
	archivo.close()	
#aqui termina ppm cifra

#####################################################################
#																	#
#																	#
#																	#
#				AQUI INICIA PPM DESCOMPRIMIR						#
#																	#
#																	#
#																	#
#####################################################################

#aqui inicia ppm descifra

def leerppmd(r):
	archivo=open(r,'r')
	texto=archivo.readline()
	cont=0
	while texto !="":
		if cont==0:
			form=texto
			texto=archivo.readline()
			cont=cont+1
		elif cont==1:
			text=texto.split(" ")

			col=text[0]
			fil=text[1]
			texto=archivo.readline()
			cont=cont+1
		elif cont==2:
			maxs=texto
			texto=archivo.readline()
			cont=cont+1
		elif cont>2:
			cod=texto.split(" ")

			descomprimeppm(form,fil,col,maxs,cod)
			texto=archivo.readline()
		
def descomprimeppm(form,f,c,m,cod):
	arr=""
	cont=1
	aux=0
	col=0
	for i in cod:
		if cont==1:
			val=i;
			cont=cont+1
		else:
			x=int(i)
			for j in range(x):
				
				g = len(arr)/3
				if g < c:
					arr = arr+str(val)+" "
				else:
					arr = arr+"\n"
			cont=1;

	archi=open('descifradoRLE.ppm','w')
	archi.write(form)
	archi.write(str(f)+" "+str(c)+"\n")
	archi.write(m)
	archi.write(arr)
	archi.close()



#####################################################################
#																	#
#																	#
#																	#
#				AQUI SE EJECUTA EL MENU PRINCIPAL					#
#																	#
#																	#
#																	#
#####################################################################

print "Bienvenido, este programa le permitira comprimir y descomprimir un archivo de texto con formato RLE\n"
print "Menu de opciones\n1 - Archivo de texto\n2 - Imagen PPM"
general = int(raw_input());
if(general == 1):
	opcion = 1
	while opcion != 3:
		print "Menu del archivo de texo\n1 - Comprimir\n2 - Descomprimir\n3 - Salir"
		opcion = int(raw_input())
		if(opcion == 1):
			print "Ingresa la ruta del archivo de texto para comprimir"
			r = raw_input()
			leer(r)
		elif(opcion == 2):
			print "Ingresa la ruta del archivo de texto para descomprimir"
			r = raw_input()
			dec(r)

elif(general == 2):
	opc=0
	while opc != 3:
		print "Menu del archivo PPM\n1 - Comprimir PPM\n2 - Descomprimir PPM\n3 - Salir"
		opc = int(raw_input())
		if(opc == 1):
			print "Ingresa la ruta del archivo PPM para comprimir"
			ruta = raw_input()
			leerppm(ruta)
		elif(opc == 2):
			print "Ingresa la ruta del archivo de PPM para descomprimir"
			ruta = raw_input()
			leerppmd(ruta)