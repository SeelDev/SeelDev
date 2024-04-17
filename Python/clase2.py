#---------------------
# 		Clase 2
#---------------------
'''
print('Division entera  es' , 10//9)#1
print(" divi solo resto es" , 10%4) #2
'''

#-----------------------------
# OP DE ASIGNACION (=)
#-----------------------------
#EL RESULTADO DE UNA OPERACION SE ASIGNA A UNA VARIABLE.
#variable: espacios de memoria RAM
'''

nombre = "Python"

print(nombre)

nombre = "Carlos"

print(nombre)

'''
#variables  de tipado dinamico
'''
a=10	
A= "dias"
b= 20.5
c = a*b
d = "python"
e = True



#op aritmetica
print("la suma de las variables es : ", a+b)
print("la multi de las variables es : " , a*b)
print("la multi de las variables c es : " ,c)
'''

#--------------------
#	type
#--------------------
#print= imprimir el codigo a ejecutar

'''
print( 'el tipo de variable es' ,type(a))
print( 'el tipo de variable es' ,type(b))
print( 'el tipo de variable es' ,type(c))
print( 'el tipo de variable es' ,type(d))
print( 'el tipo de variable es' ,type(e))
'''

#--------------------
#	BUENAS PRACTICAS
#--------------------
'''
python diferencia entre minuscula y MAYUSCULAS
print( 'el tipo de variable es' ,type(A))


lowerCamelCase 
velocidadMaxima = 100
las var no pueden empezar con caracter especial, ni numero

variables mas descriptivas
nombreDelCurso= 'python'

cuando el nombre de la variable este en MAYUSCULAS se refiere a una CONSTANTE

VEL_MAX = 100
IVA= 1.21
PI= 3,14
'''


#-----------------------
#	OP DE COMPARACION
#-----------------------
'''
a= 6
b= 23
c = 4
#igualdad
print(10==2*5)
print(10 != 7)
print(5>a)
print( 4 >= c)
print (200< b)
print (a <= b)
'''

#---------------------------
#	OP LOGICAS AND, OR , NOT 
#---------------------------
'''
#conjuncion
a = 10 
b= 20
c=5

print (a < b and c <  a )

print (a < b or c <  a )
'''
#--------------------------------
#	metodos cadena de caracteres
#--------------------------------
'''
var = " nombre de usuario" 
print (var)
print (len (var)) #contar caracteres


print (var.upper)#cambiar a mayuscula

print (var.lower) #letras minusculas

print (var.count('o')) #contar letra especifica

print (var.find('m')) #encontrar letra en su posicion

print (var.replace("!", "? "))#reemplazar caracter

#concatenar

saludo = "Hola,"
nombre = "Jose"

print (saludo + " "  + nombre)
'''




#-----------------------------------------------------------------------
'''
print ("23" < "M") #cuando hay comillas hay un caracter, no un numero 
#" 2 y 3 " 


print ("Jose" < "Josefa") #true porque cuenta los caracteres , "jose tiene 4 " y "josefa tiene 6"
 
 '''
 
 
#----------------------------------------------------------------------- 
