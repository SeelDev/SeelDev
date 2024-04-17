#--------------------------------
#	       CLASE 8
#--------------------------------



ejercicios con funciones

volumen de la esfera --> volumen =(4/3) *pi* radio**3

volumen del cilindro ---> volumen = PI *radio ** 2 * altura

volumen de cubo ---> volumen = lado ** 3
 
radio = input
altura = input




PI = 3.14

def volumenEsfera():
	radio = int(input("defina el valor del radio en un numero entero"))
	print("el volumen de la esfera es: ", (4/3) * PI ** radio ** 3)
	
#volumenEsfera()

print("-------------------------------------")

def volumenDelCilindrio() :
	radio = int(input("defina el valor del radio en un numero entero"))
	altura = int(input("defina el valor de la altura en un numero entero"))
	print("el volumen del cilindrio es : ",  PI* radio ** 2 * altura)
	
#volumenDelCilindrio()

print("-------------------------------------")

def volumenDeCubo():
	lado = int(input("defina el valor del lado en un numero entero"))
	print("el volumen del cubo es : " , lado ** 3 )
	
volumenDeCubo()

#menu 


while True :
	seleccionar = input(" calcular: 1) esfera, 2) cilindro, 3) cubo , 4) salir ")
	if seleccionar == "1" :
		volumenEsfera()
	elif seleccionar == "2" :
		volumenDelCilindrio()
	elif seleccionar == "3" :
		volumenDeCubo()
	elif seleccionar == "4" :
		print("salir")
		break
	else :
		print("no selecciono bien")


#---->return<----


def operacion(a, b):
	suma = a+b
	resta = a-b
	lista = [suma , resta]
	return lista #hay un solo return
	
print(operacion(10,5))


--->entorno de variable<----

a = 10 <--- variable global / sirve en fuera y adentro de la funcion/ se modifica en todo los programas

def f():`
	a=1
	print(a)<---variable local/ se modifican solo en esta funcion
	
f()

print(a) <---- porque la variable "a" solo vive dentro de la funcion



buena practica ---> crear variables unicamentes en el ambito en el que son requeridas



-------------bibliotecas------------------------------
libreria ---> conjunto de implementaciones funcionales codificadas con un lenguaje de programacion
contienen rutinas creasas que proporcionan ayuda a los programadores 
pasan a formar parte del cod ppal. y por lo tanto se escribe menos codigo




LIBRERIAS EXTERNAS DE PYTHON : https://docs.python.org/es/3/library/index.html


#importar el nombre de la libreria 


#fecha y hora

import time 

print("la fecha de hoy es :" , time.asctime())

print("hola")
time.sleep(4)#tiempo de espera 
print("chau")



import time
while True :
	print("rojo")
	time.sleep(2)
	print("amarillo")
	time.sleep(2)
	print("verde")
	time.sleep(2)



#---numeros aleatorios----
#libreria ; random

#ejemplo : un sorteo 
import random
for i in range(1, 21):
	print(i , ")" , random.randrange(101))#numero aleatorio entre el rango de 0 - 10 


#ejemplo : valor de dados 

import random
import time
apuesta = int(input("que valor del dado apuesta"))
for i in range(5):
	print("tirar el dado...")
	time.sleep (2)
	valorDado = random.randrange(1,6)
	print("el valor del dado es : ")
	if apuesta == valorDado :
		print("GANASTE MUCHOS DOLARES")
		break
	else : 
		print("perdiste")



# ruleta 

apuesta = int(input("que valor del dado apuesta"))

print("tirar la bola...")
time.sleep (2)
valorDado = random.randrange(37)
print("el valor del dado es : ", valorDado)
if apuesta == valorDado :
	print("GANASTE MUCHOS DOLARES")
	
else : 
	print("perdiste")






#funcion : recibe numero q quiero ,retorno ganaste/ perdiste 
import time
import random

def timbera():
	nApuesta = int (input("que valor apuesta? 0 - 10 "))
	print("tirar numero...")
	time.sleep(2)
	valorN = random.randrange(11)
	print("el valor ganador esss...!!! ",  valorN)
	if nApuesta == valorN :
		print("felicidades!! te ganaste el telekino!!!!!")
	else :
		print("no quedaste ni en vacante flaco")
		
for i in range(3) :
	timbera()
	
	

#no tan piola
while True :
	timbera()




import random
opciones = ["piedra" , "papel" , "tijera"]

opcionAleatoria = random.randrange(3)
cpu = opciones[opcionAleatoria]
#print(opcionAleatoria)
#print("la opcion elejida es : " opciones[opcionAleatoria])

gamer = int (input("ingrese 0) piedra , 1) papel, 2) tijera"))
seleccionPersona = opciones[gamer]

if seleccionPersona == cpu :
	print("empate")
elif seleccionPersona == "piedra" and cpu == "tijera":
	print("ganaste")
###SEGUIR EL CODIGO PARA EL JUEVES


