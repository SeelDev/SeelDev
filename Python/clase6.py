#--------------------------------
#	       CLASE 6 
#--------------------------------

#--------BUCLE FOR ------
#CONTROLAR LA CANT DE VECES QUE SE REPITE EL CODIGO
#FOR RECORRE LA CANTIDAD DE ELEMENTOS QUE HAYA EN UNA LISTA 

alumnos = ["julian", "matias" , "martin" , "pablo"]


for i in alumnos :
	print("hola" , (i))
	#print(i)




#---------------------------------------------------------------------


temperaturas  = [22,44,77,1,9]
contenedor = 0

for nano in temperaturas:
    #print (nano)
    contenedor = contenedor + nano
    print (contenedor / len(temperaturas))
print ( sum(temperaturas)/len(temperaturas))

temperaturas  = []



n = 0
while temperaturas > 5 :
	if n > 5 : 
		input('Elemento a agregar a la lista' )
		print(temperaturas)



for i in temperaturas:
	contador = contador +i
	print(contador / len(temperaturas))

#----ingresar una palabra y saber cuantas letras tiene-----

while True : 
	contador = 0
	opcion = input ("quiere ingresar una palabra? s/n")
	if opcion == "s":
		palabra = input("Ingrese palabra")

		for i in palabra :
			contador = contador +1

		print("lacant de letras de la palabra " , palabra, "es" ,  contador)
	else :
		print("bueno chau")
		break

for i in "PYTHON" :
	if i == "N":
		continue #se saltea el bucle , se puede poner en el for y en el while
		break
	else:
		print(i)


conta=0
for line in open("myfile.txt"): #abrir un archivo externo
   print(line)
   conta = conta+1
  
print ("la cant de lineas es de : ", conta)




#--- bucle for anidado ----

for i in "hola":
	print("1-" , i)
	for j in "chau":
		print("2-" , j)
		for w in "Juan":
			print("3-" , w)



#tuplas 
#diccionarios
#agrupan objetos bajo un mismo nombre




#-----TUPLAS----
#Las tuplas son arrays CONSTANTES, no se pueden modificar

#Provincia = ("Mendoza", "San Juan", "La Pampa")

ver elemento

print(Provincia[1])

 

#DICCIONARIO = clave un str o Number (int, float), no tienen ordenamiento ni indice


diccionario = { "nombre" : "Juan", "id": 1}

#ver elemento

print (diccionario["nombre"])








equipo = {1 : "Barco", 2: "Menentiel" , 3 : "Romero" ,4 : "Cavani" , 5: "Messi"}

print(equipo[1],equipo[2], equipo[3],equipo[4],equipo[5])

camiseta = int( input("Ingrese numero de camiseta"))

print(equipo[camiseta])

#reemplazar elemento 
equipo[1] = "marcelo"

#agregoelementos

equipo [4] = "juan"
