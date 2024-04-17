#--------------------------------
#	        MODULO 1 
#--------------------------------


#------------------------------------
# ejercicio 1 
'''
En un script de Python, crear tres variables
nombradas a, b y c con valores numéricos
cualesquiera; una cuarta llamada resultado que
sea la suma de las primeras tres, y por último
imprimir en pantalla cada una de ellas.
'''
#------------------------------------


a = 3
b = 23
c =  34

print ("a : " )
print(a)
print ("b : ")
print(b)
print ("c : ")
print(c)

print ("resultado")
print(a + b + c)

#------------------------------------
# ejercicio 2
'''
Crear dos variables, saludo y nombre, cuyos
contenidos sean "Hola, " en el primer caso y tu
nombre en el segundo. Intenta sumarlas vía el
operador + y mostrar el resultado en pantalla. 
'''
#------------------------------------


saludo = "Hola , "

nombre = "Selene"

print(saludo + nombre)




#--------------------------------
#	       CONDICIONALES 
#--------------------------------



#--------------------------------
#	        ejercicio 1
'''
Armar una frase con las 3 variables dadas y
mostrarla por pantalla.
'''
#--------------------------------


texto_uno = "potente"
texto_dos = "sol"
texto_tres = "triunfo"

print("Que" , texto_tres , "es poder ver el ", texto_dos , "tan " , texto_uno , "a la maniana por despertarte temprano" )





#--------------------------------
#	       ejercicio 2 
'''
Realizar un programa que tenga 2 variables,
base = 10 y altura = 5, calcular el área de
un rectángulo y mostrar por pantalla.
'''
#--------------------------------


base = 10
alt = 5

print("el area de un rectangulo es " , base * alt )



#--------------------------------
#	       ejercicio 3
'''
Dadas 2 variables: a = 20 y b = 10, mostrar por
pantalla su suma, resta, multiplicación y división.
'''
#--------------------------------


a = 20
b = 10

print ("La suma entre a y b es : ", a + b)
print ("La resta entre a y b es : " ,a - b)
print ("La multi entre a y b es : ", a * b)
print ("La div entre a y b es : ", a / b)





#--------------------------------
#	       DESAFIOS 
#--------------------------------


#--------------------------------
#	       ejercicio 1
'''
 Tomás rindió 3 exámenes, se desea saber su
promedio
'''
#--------------------------------
nota_uno = 10
nota_dos = 6
nota_tres = 8


promedio = ((nota_uno + nota_dos + nota_tres) / 3)


print("El promedio de tomas es : " , promedio )





#--------------------------------
#	       ejercicio 2
'''
 Hacer un programa que determine si una
persona es menor de edad o mayor de edad,
teniendo la edad en una variable.
Probar el código cambiando el valor de la
variable “edad
'''
#--------------------------------

edad = 5

if edad >= 18 :
	print("Sos mayor de edad")
else :
	print("Sos menor de edad")





#--------------------------------
#	       ejercicio 3
'''
 Un empleado cobró 300 dólares por mes desde enero
a junio, 500 dólares de julio a octubre, y 700 dólares
por mes en noviembre y en diciembre.
Hace un programa que calcule el sueldo promedio. Y
que diga si este “empleado” está cobrando un sueldo
bajo, normal o mejor de lo normal.
● Sueldo bajo: por debajo de 300 dólares.
● Sueldo normal: entre 300 a 900.
● Sueldo mejor de lo normal: más de 900 dólares.
'''
#--------------------------------


sueldo_total = 300 * 6 + 500 * 4 + 700 * 2
promedio = sueldo_total / 12
print("El sueldo promedio es:",promedio)


'''
sueldoBajo = 350.23 #menos de 300 dolares
sueldoNormal = 233.5
sueldoMejor= 300
'''
# promedio = float((sueldoBajo + sueldoNormal + sueldoMejor ) /3)
#print(promedio)

if promedio >= 0 and promedio <= 300 :
	print("tu sueldo es bajo")
elif promedio >= 300 and promedio <= 900:
	print("tu sueldo es normal")
elif promedio >= 900 :
	print("tu sueldo es mejor de lo normal")

else:
	print("datos incorrectos ")
