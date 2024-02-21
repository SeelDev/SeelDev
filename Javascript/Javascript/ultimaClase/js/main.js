//-------------------------------------------
// Zona de declaración de variables
//-------------------------------------------

var estadoSemaforo = 0 // 0 = rojo
// 1 = rojo-amarillo
// 2 = verde
// 3 = amarillo


var modoAutomatico = false 


var reftTimer 
//-------------------------------------------
// Zona de declaración de funciones
//-------------------------------------------
function encenderLuz(id, prender) {
    var color = prender ? id : '#333'

    document.getElementById(id).style.backgroundColor = color
}

function cambiarEstado() {
    console.log('estadoSemaforo', estadoSemaforo)

    switch (estadoSemaforo) {
        case 0:
            encenderLuz('red', true)
            encenderLuz('yellow', false)
            encenderLuz('green', false)
            break;
        case 1:
            encenderLuz('red', true)
            encenderLuz('yellow', true)
            encenderLuz('green', false)
            break;
        case 2:
            encenderLuz('red', false)
            encenderLuz('yellow', false)
            encenderLuz('green', true)
            break;

        case 3:
            encenderLuz('red', true)
            encenderLuz('yellow', true)
            encenderLuz('green', false)
            break;
       
       
        default: 
            encenderLuz('red', true)
            encenderLuz('yellow', true)
            encenderLuz('green', true)
            estadoSemaforo = 0
           // break;


    }

    estadoSemaforo++
    if (estadoSemaforo > 3) estadoSemaforo = 0
}

function cambiarModo() {
 modoAutomatico = !modoAutomatico
 console.log('cambiarModo' , modoAutomatico)

document.querySelector('h4').innerText = modoAutomatico? 'Modo AUTOMATICO' : 'Modo manual'
document.querySelector('button').disabled = modoAutomatico
 if( modoAutomatico){
    reftTimer = setInterval(cambiarEstado, 2000) // buscar mas info 
 }
 else{ 
    clearInterval(reftTimer)
 }
}





function start() {
    console.warm(document.querySelector('title').innerText)

    encenderLuz('red')
    encenderLuz('yellow')
    encenderLuz('green')

}

//-------------------------------------------------------------
// Zona de ejecucion (punto de entrada donde inicia el programa)
//-------------------------------------------------------------

start()
