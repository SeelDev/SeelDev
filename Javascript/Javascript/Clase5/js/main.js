var persona = { 
    nombre:  'Juan',  // propiedad // equivalentes a una variable
    edad: 23,          // propiedad // equivalentes a una variable
    saludar: function(){  //funcion anonima// metodo // equivalente a una funcion
        return 'Hola como estan?'
    }
}

console.log(persona)



///////

console.log(
    //Strings//
)

var saludo = 'Hola mundo'
console.log(saludo, typeof saludo)





////// metodos de los arrays

var numeros = [ 88, 11, 23, 56 , 78, 33]
console.log(numeros)

console.log('La cantidad de elementos que tiene " [' + numeros + ']" es ' + numeros.length)


// 4 metodos de array

console.log(/*  push */)
numeros.push(77)  // incorpora objetos al final del listado del array
console.log(numeros)


console.log(/*  unshitf */)
numeros.push(55) // incorpora objetos al principio del listado del array
console.log(numeros)



console.log(/*  pop */)
numeros.push(77 ) // saca objetos del listado del array
console.log(numeros)


console.log(/*  shift */)
numeros.push(55 ) // saca objetos del principio del listado del array
console.log(numeros)



console.warn(/* reverse */)
console.log(numeros)
console.log(numeros.reverse()) // invierte las posiciones de los objetos, se espejan 
console.log(numeros)




// ejemplo con split, reverse y join ;  para invertir los caracters de un string

var mensaje = 'Hola como estan'

var mensajeAlReves = mensaje.split( ' ' ).reverse().join(' ') // ejecucion en chainig

//espaciador del string join()

console.log(mensaje)
console.log(mensajeAlReves)


// metodos avanzados

numeros = [ 1, 2, 3, 4, 5,]
console.warn(/* map */) // genera un array  nuevo, no modifica el existente
console.log(numeros)
 var numerosX3 = numeros.map(function(elemento) {return elemento})  // colback

console.log(numeros)
console.log(numerosX3)




//



















