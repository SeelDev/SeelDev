#--------------------------------
#			CLASE 3
#--------------------------------

'''
< : menor
> : mayor  

'''

#-----------------------------------------------------------------------
'''
#ANIDADOS
# es necesario pasarlo a entero o a flotante 

temperatura = int (input("ingrese la temperatura actual"))
humedad = int (input( " ingrese la humedad actual"))

if temperatura <0:
	print("Congelado")
	if humedad > 78:
		print("nieve")
	else:
		print("hielo")
		
elif temperatura < 10 and temperatura >= 0: 
	print ("hace frio")
	if humedad > 60 :
		print (" llovizna y llevo paraguas")
	else: 
		print (" solo me abrigo ")

elif temperatura < 20  and temperatura >= 10 :
	print ("templado")
	if humedad > 55:
		print(" puede que llueva")
	else: 
		print("voy a tomar un cafe")
		
elif temperatura <=30 and temperatura >= 20 :
	print (" hace calor ")
	if humedad >= 40 :
		print (" unas ganas de que llueva")
	else :
		print (" me meto a la pile")
		
else :
	print (" es un infierno ")
	if humedad > 80 : #if anidado
		print(" traigan el arca llueve")
	else:
		print ("lleno de nubes")


'''

	
#-----------------------------------------------------------------------	





''' nota > 8
nota = 6.5

if nota > 8 :
	print("aprobado" )
else :
	print ("desaprobado")
'''	
	
	
	
	#PROMEDIO (sumar notas) dividido 3 
'''
nota1= -100
nota2= 6
nota3= 4

promedio = ((nota1 + nota2 + nota3) / 3)
print(promedio)

if promedio >= 7 and promedio <= 8:
	print ("bueno")
elif promedio >= 8 and promedio <= 9:
	print(" Muy bueno" )
elif promedio >= 9 and promedio <= 10 :
	print(" Excelente" )
elif promedio > 10  or promedio < 0:
	print("Mal nota")
	
else :
	print ("afueraa")
'''
	
	
	

'''
#--------------------------------
#	SISTEMA DE AUNTENTICACION
#--------------------------------
#str convierte a un numero a un string
#password = int (password) cambia de string a entero 
input("bienvenido")

usuario =  input("ingrese un usuario")#tomar lo que ingrese por teclado como un string
password = int (input("ingrese clave")) #agregar int o float al input  para ahorrar lineas de codigo

#usuario = "pepe"
usuario = usuario.upper() #mayusculas
#password = "1234"
#password = float  (password) = convierte a numero con coma





if usuario == "PEPE" and password == 1234:
	print(" bienvenido" )
elif usuario != "PEPE" :
	print(" ingreso mal el usuario - ACCESO DENEGADO")
else :
	print(" ingreso mal la contra - ACCESO DENEGADO")
'''
	
#-----------------------------------------------------------------------
