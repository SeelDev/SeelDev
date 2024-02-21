
//-------------------------------
// xona de declaracion de variables
//-------------------------------


var input

//-------------------------------
// xona de declaracion de funciones
//-------------------------------
function leerInput ( ){
    //console.log('ESCRIBI ALGO...')

    input = document.querySelector('input')
    var contenido = input.value
    console.log(contenido)

    var parrafos = document.querySelectorAll('div p')
//selector css dependiente
   parrafos[0].innerText = contenido.split('').reverse('').join('')
   parrafos[1].innerText = contenido.toLocaleUpperCase()

}
function start( ) { //window.onload = evento 
    console.log('documento web esta totalmente cargado')

   input = document.querySelector('input')
console.log('input')


input.oninput = leerInput
} 


//-------------------------------
// xona de start
//-------------------------------



window.onload = start 