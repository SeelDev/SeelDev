console.log(
    /* ARRAYs */
)


var numero = 81
console.log(numero, typeof numero)
// indice =    0 1 2 3  4
var numeroS = [1,2,3,3,888]// array homogeneo, contiene el mismo tipo de dato; tipo Number //lista de numeros(elementos)
console.log(numeroS, typeof numeroS, Array.isArray(numeroS))
console.log('El array de numeros tiene ' + numeroS.length + ' elementos')



var primerElemento = numeroS[0]
console.log(primerElemento)

var ultimoElemento = numeroS[numeroS.length-1]
console.log(ultimoElemento)

numeroS[4] = 99
console.log(numeroS)
console.log(numeroS[4])

for(var i=0 ; i<numeroS.length; i++){ 
    console.log('El elemento de indice ' + i + 'cintiene l valor ' + numeroS[i])
}





// 
var diaSemana = [           // array homogeneo; datos tipo string
    'domingo',      //indice 0
    'lunes',        //indice 1
    'martes',       //indice 2
    'miercoles',    //indice 3
    'jueves',       //indice 4
    'viernes',      //indice 5
    'sabado'        //indice 6
]

var numDia = new Date(). getDay() // 0: domngo ... 6: sabado
//console.log(numDia)
var nombreDia = diaSemana[ numDia ]
console.log('Hoy es dia ' + nombreDia)



// array heterogeneo contiene distintos tipos de datos en una misma estructura
//indice =              0       1       2       3
var arrayPersona = [ ' juan' , 'perez' , 23 , true]
console.log(arrayPersona, typeof arrayPersona, Array.isArray(arrayPersona))

//acceso a la info dentro del array utilizando sus indices con []

console.log('La persona se llama ' + arrayPersona[0] + ' ' + arrayPersona[1] +
 ' y tiene ' + arrayPersona[2] + 'tiene anios de edad')

 //Array.isArray(arrayPersona) verdadero si es un array  []     &&       falso si es un objeto {}







 ///////////////////////
 console.log(
    /* OBJETOS! */
 )



 //clave/ valores >     c         v         c           v       c   v       c      v
var objetoPersona = { nombre: ' juan' , apellido:  'perez' , edad: 23 , acceso: true } //claves
console.log(objetoPersona, typeof objetoPersona, Array.isArray(objetoPersona))




//acceso a la info dentro del objeto utilizando sus claves con sintaxis corchete [] sin importar el orden 
console.log('La persona se llama ' + objetoPersona['nombre'] + ' ' + objetoPersona['apellido'] +
 ' y tiene ' + objetoPersona['edad'] + 'tiene anios de edad')



//acceso a la info dentro del objeto utilizando sus claves con sintaxis con punto sin importar el orden 
console.log('La persona se llama ' + objetoPersona.nombre + ' ' + objetoPersona.apellido +
 ' y tiene ' + objetoPersona.edad + 'tiene anios de edad')



 console.LOG(/* ARRAY DE OBJETOS */)

 var personas = [
    { nombre: ' juan' , apellido:  'perez' , edad: 23 , acceso: true },
    { nombre: ' sele' , apellido:  'urdi' , edad: 19 , acceso: true },
    { nombre: ' lala' , apellido:  'pi' , edad: 45 , acceso: false },
    { nombre: ' fina' , apellido:  'ju' , edad: 32 , acceso: true }

 
]

console.log(personas, typeof personas, Array.isArray(personas) )


for(var i=0; i<personas.length; i++){
    console.warn('Persona nro. ' + (i+1))

    console.log(personas[i])



//sintaxis.punto
    console.log('La persona se llama ' + personas[i].nombre + ' ' + personas[i].apellido +
    ' y tiene ' + personas[i].edad + 'tiene anios de edad')
//sintaxis[]
    console.log('La persona se llama ' + personas[i]['nombre'] + ' ' + personas[i]['apellido'] +
    ' y tiene ' + personas[i]['edad'] + 'tiene anios de edad')
   

}


/* FUUUUNNNNNCCCCIIIIOOOONNNNEEESSSS */

var diaSemana = [           // array homogeneo; datos tipo string
    'domingo',      //indice 0
    'lunes',        //indice 1
    'martes',       //indice 2
    'miercoles',    //indice 3
    'jueves',       //indice 4
    'viernes',      //indice 5
    'sabado'        //indice 6
]


var numeroS = [1,2,3,3,888]





