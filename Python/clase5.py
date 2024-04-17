#--------------------------------
#	        CLASE 5 
#--------------------------------

#<-----listas de objetos---->

#lista llamada temperaturas


#ver objeto dela lista



'''
numeros = [12,15,35,2]

#cantidadnumeros=len(numeros)
#print (cantidadnumeros)

#sumatoria = numeros[0]+numeros[1]+numeros[2]+numeros[3]
posicion= 0
sumatoria =0
while True:
	
	if posicion >= len(numeros):
		print ("El prom es: ", sumatoria/len(numeros))
		break
	else:
		sumatoria = sumatoria + numeros[posicion]
		posicion = posicion +1
'''	
'''		
temperaturas = [12,14,56,34.2,6,18,19, "listas", ["a", "B", "C"] ]
#indice  	    0   1  2   3  4  5  6 		7 8 =  0    1     2	
print(temperaturas [8][2])		
#agregar objetos en la lista en ultima posicion

temperaturas.append(3333)
print(temperaturas)


#corre todos los elementos para posicionar en i

temperaturas.insert("pepe")


#pisar valor

temperaturas[1] = "juan"


#crear sin elementos 
temperaturas = []


#borrar el ultimo  elemento
temperatura.pop()
#borrar un elemento
del temperaturas[3]
#borrar el primer  elemento espeficio ain importar el indice, el primero que encuentra
temperaturas.remove(23)
'''

#-----------------------------------------------------------------------

'''
ingrese 5 temps para llenarlo en la lista

'''
'''
contador = 0 
lista = []
while contador < 5 :
	ingresodeTemps = int (input ("agregue una temperatura"))
	lista.append(ingresodeTemps)
	contador = contador + 1

print(lista)
temperaturas=[12,44,23,26,77]

print("La lista de temperaturas es: ", temperaturas)
print("El valor maximo de la lista es: ",max(temperaturas)) maximo
print("El valor minimo de la lista es: ",min(temperaturas)) minimo
print("El valor promedio de la lista es: ",sum(temperaturas) sumatoria /len(temperaturas))

'''
nombres = ["pepe" , "jose", "luis",  "armando"]

#ordenar alfabeticamente primero por mayusc y dps por minusc solo strings

nombres.sort(reverse = True)
print(nombres)



#<------MATRICES----->

#LISTAS DENTRO DE LISTAS
