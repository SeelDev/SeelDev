// Formas de incrementar una variable(sumarle 1)
console.warn('/* forma normal */')

var n = 9
n = n + 1
// n = n + x
// n += x
// n -= x
// n *= x
// n /= x
// n %= x
// n += x
console.log(n)
////
console.warn('/* forma reducida */')

n = 9
n +=  1
// n += x
// n -= x
// n *= x
// n /= x
// n %= x
// n += x

console.log(n)
///////
console.warn('/* forma post incremento */')
//n++ : suma de a 1 
n = 9
 var postInc = n++
 //++n 
 // n-- (post decremento)
 // n** (no existe)
 // n// (no existe)
 // n%%( no existe)
console.log(n, postInc)
//
console.warn('/* forma pre incremento */')

n = 9
var preInc = ++n  
//++n (pre decremento)
 // n-- (post decremento)
 // n** (no existe)
 // n// (no existe)
 // n%%( no existe)
console.log(n, preInc)



/* REPETICION : do while, while, for (too : c++) */

console.warm(/* Con ciclo do while:  representar los numeros del 0 al 9 en forma consecutiva */)
// hace y dps preguntaa
var numero = 0 // inicializacion
do {
    console.log( numero)
    numero++ // incrementa
}
while (numero <= 9) //contador


console.warm(/* Con ciclo while:  representar los numeros del 0 al 9 en forma consecutiva */)
// while: pregunta si entra a la estructura iterativa antes de entrar
 numero = 0 // inicializacion
while (numero <= 9) { //chequea
    console.log( numero)
    numero++ // incrementa
} // salida
 

 console.warm(/* Con ciclo for:  representar los numeros del 0 al 9 en forma consecutiva */)

//       1        2/5/8/11          4/7/10
 for (numero = 0; numero <= 9; numero++) { 
     console.log( numero) 
 }//        3/6/9
 //12

 console.warm(/* Con ciclo for:  representar los numeros del 9 a 0 en forma consecutiva */)

for(var num = 9 ; num >= 0; num--) {
    console.log(num)

}

console.warm(/* uso del break en ciclo de repeticion */)

do {
    console.log( numero)
    numero++ // incrementa
    if(numero == 6) break
}
while (numero <= 9)
console.log('/////')
//////

while (numero <= 9) { //chequea
    console.log( numero)
    numero++ // incrementa
    if(numero == 6) break
}
console.log('/////')

/////
// el continue es solo para el for 
for(var num = 0 ; num < 10; num++) {
    if(numero == 2  ) continue // chequea cuando llega al 2 y pasa al incremento
    console.log(num)
    if(numero == 6) break

}
console.log('/////')

console.warm(/* for: multiples acciones en sus campos */)


//   inicializacion (+1)   ;      test de condicion/es  ;    actualizacion/es o post ejecucion/es
for( var i = 0, j = 9      ;     i<10      &&   j>= 5        ;         i++, j--) {
    console.log(i,j)
}

console.warm(/* for: anidado */)
var contador = 0
for(var i = 10; i<15; i++){
    for(var j= 20; j<25; j++) {
        for(var k = 0; k<2; k++) {
            console.log(++contador + ':' + i,j,k)
         }
   
    }
        
}


console.warm(/* for: representar los numeros del 0 al 20 de 2 en 2 */)


for(var num=0; num<=20; num+=2) {
    console.log(num)
}

//////// ejercicio

/* for(var num=10; num <= 40; num++) {
    var tipo = ''
    if(num % 2 == 0)tipo = 'par' 
    else tipo = 'impar'
    console.log(num + '' +  tipo)

} */

for(var num=10; num <= 40; num++) {
    var result = 
    num  + '' +  
    (num % 2 == 0 ? 'par ' : 'impar') + ' ' +
    (num % 3 == 0 ? '* ' : '')  + ' ' +
    (num % 5 == 0 ? '# ' : '') 
    
    console.log(result)

}
// todo tiene que ser numerico para que sea una suma aritmetica
// promedio de notas 
console.warn('\n/*  calcular el promedio de las notas de alumnos(do / while) */')
do {
    var sumatoriaNotas = 0
    var cantidadNotas = 0
    var notasAcumuladas = ' '
    var nombre = prompt('Ingrese el nombre del alumna')
    do{ 
    var entrada = prompt('Ingrese la nota del alumno' + nombre + ' para finalizar pulse CANCEL')
        if (entrada == null) break
                
            var nota = Number(entrada)
            if(nota >= 0 && nota <= 10 ){
                sumatoriaNotas += nota // sumas
                cantidadNotas++ // contador 
                notasAcumuladas += ( nota + ' ') // NOTAS ACUMULADAS // dejar lugar p/ q no se peguen los numeros     
            }

            else{ 
                alert('La nota ' + nota + ' no es valida')
            }
        
            
        
    }
    while( entrada != 'f')
        if( cantidadNotas != 0 ){ 
    var promedio = sumatoriaNotas / cantidadNotas

    console.log(
        '\n' +  ' La cantidad de notas ingresadas ' + cantidadNotas + '\n' +
        '\n' + 'Las notas son: ' + notasAcumuladas + '\n' + 'El promedio de las notas ingresadas es ' + promedio + '\n' +
        'La alumna ' + nombre + ' ' +  (promedio >=4 ? 'Aprobo' : 'No aprobo') + '\n' 
    )
    }
    else {
        alert('No se pudo calcular el prom, ya que no hay notas')
    }
 }
 while (confirm( ' Desea calcular otro promedio?'))