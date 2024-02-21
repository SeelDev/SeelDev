//---------------------------------------------------------
//            proyecto integrador 
//---------------------------------------------------------

const costoBaseM2 = 75.40 
console.log(costoBaseM2, typeof costoBaseM2)

let totalMetrosCuadrados = +prompt('Ingresa el total de metros cuadrados de la vivienda o comercio que desea cotizar.')
console.log(totalMetrosCuadrados, typeof totalMetrosCuadrados)

let fm = 1.005 // factor multiplicador para un PH
console.log(fm, typeof fm )

let resultado = fm * costoBaseM2 * totalMetrosCuadrados


alert('El monto total de la poliza es ' + resultado)

