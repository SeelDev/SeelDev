#--------------------------------
#	       CLASE 7
#--------------------------------
futbolistas = {
    1 : "Dibu Martinez", 15 : "Montiel",
    3 : "Acuña", 5 : "Paredes",
    11 : "Di Maria", 14 : "DE Paul",
    16 : "Otamendi", 8 : "Guido Rodriguez",
    10 : "MESSI", 6 : "Fernandez",
    7 : "LAUTARO MARTINEZ"
}

#ver diccionario completo
#print(futbolistas)


#.items() = trae la clave y el elemento
for camiseta , jugador in futbolistas.items():
	print(camiseta , "->" , jugador)


#len cuenta elementos, no claves
print("La canti de jugadores es :", len(futbolistas))

#atrae solo las claves del diccionario
print("camisetas", futbolistas.keys())


#trae solo los elementos/ valores del diccionario
print("los nombres de los jugadores", futbolistas.values())


#----ejercicio----

#ingrese numero de camiseta del jugador que fue la figura del partido 

jugadorFigura = int (input("ingrese la camiseta del jugador del partido"))
#print("el juego figura fue :" , futbolistas [jugadorFigura])

#get(tomar), si la clave existe, devuelve valor, si no devuelve este codigo
elem = futbolistas.get(jugadorFigura, "esta camiseta no existe")
print("el jugador figura fue :" , elem)


#----ejercicio---

#cambio de jugador , di maria y poner BARCO

futbolistas[11] = "Barco"

print(futbolistas)


#borrar elemento del diccionario : pop
expulsado = int (input("jugador expulsado:"))
print("el jugador expulsado:" , futbolistas.pop(expulsado , "esa camiseta no existe"))

for nombres in futbolistas.values():
	print(nombres)

#borrar todos los elementos

futbolistas.clear()
print("eliminamos todos los jugadores" , futbolistas)




#op(membership) de pertenencia para la clave =  in - not in (si estan en colecciones) respuesta: boolean


# comprobar ingreso numerico (salvar valor)

isdecimal() si tengo str, lo puedo convertir a int? boolean / FORMA LARGA de convertir de str a int/ control si es numero o no




futbolistas = {
    1 : "Dibu Martinez", 15 : "Montiel",
    3 : "Acuña", 5 : "Paredes",
    11 : "Di Maria", 14 : "DE Paul",
    16 : "Otamendi", 8 : "Guido Rodriguez",
    10 : "MESSI", 6 : "Fernandez",
    7 : "LAUTARO MARTINEZ"
}


jugadorFigura = input("ingrese la camiseta del jugador del partido")

if jugadorFigura.isdecimal() == True :
	jugadorFigura = int (jugadorFigura)
	print("el juego figura fue :" , futbolistas [jugadorFigura])
else :
	print("no ingreso un int")
	
#si hay posibilidad de que haya numeros float, usar float, y poner todos los numeros en flotantes 7.0


#-----------------------------------------------------------------------


# lista de numeros correlativos enteros
#temperaturas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#INSTRUCCION range()(rango)crea una lista sin necesidad de definirla=  numeros correlativos y enteros
for i in range(10) : #[0 ; (n)-1]
	print(i)

for i in range(5, 15,2) : #[5 ; (15)-1] ",2" -> va de dos en dos
	print(i)


#numeros impares desde 0 - 20 [1(p/ numeros impares), 20 , 2]


for i in range(1 , 20 , 2) :
	print(i)

for i in range(20 , 1 , -2) :
	print(i)

	
#cuenta regresiva 10 - 0

for i in range(10, -1 , -1) :
	if i == 10 :
		print(i , "despegue")
	elif i == 5 :
		print(i , "mitad")
	elif i == 3 :
		print(i, "enciendan motores")
	elif i == 0:
		print(i , "despegue")
	else:
		print(i)

inicio = int(input("valor inicial"))
final = int (input("valor final"))
salto = int (input("salto"))

for i in range(inicio ,  final , salto):
	print(i)



#--------------------------------
#	       FUNCIONES
#--------------------------------

agrupar codigo
def: definir una funcion
- def etiqueta (argumento/parametro): lineas
		de
		codigo
		
los argumentos solo tienen valor dentro de la funcion; deben ser pocos argumentos , muchos * para listas y ** para diccionario
ejecucion :

etiqueta()

-----ejemplo-----

def rangos(): 
	inicio = int(input("valor inicial"))
	final = int (input("valor final"))
	salto = int (input("salto"))

	for i in range(inicio ,  final , salto):
		print(i)
#CALL rangos();
rangos()


---ejemplo----
def nombre():
	print("hola mundo")


#for ; ejecuta 5 veces la funcion

for i in range(5):
	nombre()






# 3 funciones = resta, suma , multi



# menu =

def sumar(a , b):
	 
	#numero1 = int (input('ingrese un numero'))
	#numero2 = int (input('ingrese otro numero'))
	print("la suma es : " , numero1 + numero2)

def restar():
	
	numero1 = int (input('ingrese un numero'))
	numero2 = int (input('ingrese otro numero'))
	print("la resta es : " , numero1 - numero2)

def mult():
	
	numero1 = int (input('ingrese un numero'))
	numero2 = int (input('ingrese otro numero'))
	print("la multiplicacion es : " , numero1 * numero2)
	
	
while True :
	seleccion = input("quiere sumar (s),restar(r), mult (m) o salir(x)") #x = break
	if seleccion == "s" :
		sumar()
	elif seleccion == "r":
		restar()
	elif seleccion == "m" :
		mult()
	else :
		if seleccion == "x" :
			print("ok")
			break	



#con valores de argumentacion/ valores vivos dentro de la funcion, no se puede exportar 

def sumar(a , b):
	 
	#numero1 = int (input('ingrese un numero'))
	#numero2 = int (input('ingrese otro numero'))
	print(a)
	print(b)
	print("la suma es : " , a+b )#numero1 + numero2

sumar()

#buenas = 

def calcular(a , b):
	print("la suma es : " , a+b )
	print("la resta es : " , a-b )
	print("la mult es : " , a*b )
	
numero1 = int (input('ingrese un numero'))
numero2 = int (input('ingrese otro numero'))
calcular(numero1,numero2)


#-------------------------------------------------------------------------------------------------------------------------
