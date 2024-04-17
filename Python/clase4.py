#--------------------------------
#	        CLASE 4 
#--------------------------------
'''
numUno = int ( input (" ingrese un numero:     " ))
numDos = int (input (" ingresa otro numero:    "))

opcionOp = input(" Que operacion desea hacer? Suma, Resta o Division:      ")

if opcionOp == "suma" :
	print ("La suma entre dos numeros  son " ,  numUno + numDos )
elif opcionOp == "resta" :
	print ("La resta entre dos numeros  son " ,  numUno - numDos )
elif opcionOp == "division" :
	print ("La division entre dos numeros  son " ,  numUno / numDos )
else :
	print ("No hay operacion correcta ingresada")
	
	
#-----------------------------------------------------------------------
# hacer muchas variables es costoso a nivel memoria;
#suma = print( numUno + numDos)
#resta = print( numUno - numDos)
#division = print( numUno / numDos)
#-----------------------------------------------------------------------

'''
	
	
#-----------------------------------------------------------------------
'''
nombre= input (" ingrese su nombre    ")
apellido = input ( " ingrse su apellido    " )
	
print (" bienvenido", nombre + apellido)
# print (" bienvenido", nombre,  apellido)
'''
	


#-----------------------------------------------------------------------


#------------------------------------
# BUCLE / estructura de REPETICION
#------------------------------------

#-----WHILE---------
	#true -> repite de nuevo
	#false -> sale del bucle
	#salir = BREAK
	
#-----estructura---------

'''
while condicion : 
	verdadero -> se ejecuta el codigo
	incrementacion
'''


'''
a = 1  # acumulador

while a <= 5 :
	print ("hola mundo")
	a = a + 1 # contador 
	if a == 3 :
		print ("chauchi") 
		break #sale del bucle sin importar el conteo 
'''

'''
#nota = int (input("ingrese nota"))

while True : 
	
	nota = int (input("ingrese nota"))
	if nota < 10 : 
		print (" desaprobado ")
	else : 
		print ("aprobado " )
		break
'''
'''
tiempo = 10 
while tiempo > 0 :
	print (tiempo )
	tiempo = tiempo - 1
	if tiempo == 0 :
		print (tiempo ,"despegue")
'''

'''
tiempo = 10 
while tiempo >= 0 :
	if tiempo == 10 : 
		print (tiempo,"arrancar motores")
	if tiempo == 5 :
		print (tiempo,"mitad")
	if tiempo == 3 : 
		print (tiempo,"preparar" )
	if tiempo == 0 :
		print (tiempo ,"despegue")
	else : 
		print (tiempo)
	tiempo = tiempo - 1
    a = 10

while a >= 0:          
	if a == 10:
		print(a,"arrancar")
	elif a == 5:
		print(a,"por la mitad")
	elif a == 3:
		print(a,"sujetarse")
	elif a == 0:
		print(a,"despegue!!!")
	else:
		print(a)
	a= a - 1

'''

'''
tempUno= int (input("ingrese temperatura" ))
tempDos = int (input("ingrese temperatura" ))
tempTres = int (input("ingrese temperatura" ))
temp = 0 
while True : 
	if temp == 0 : 
		print (" promedio es " , (tempUno + tempDos + tempTres) / 3)
		break
'''

		
'''
sumatoria = 0
canttemperaturas=0
while True:
	nota = float(input("ingrese una nota"))
	if nota ==0:
		print("El promedio es:", sumatoria/canttemperaturas)
		break
	else:
		sumatoria = sumatoria + nota
		canttemperaturas = canttemperaturas+1

'''
