/// zona : definicion de variables

var empleados = [

]






/// zona : definicion de funciones




function agregar(e){
    e.preventDefault()
   // console.log('agregar')

   var refNombre = document.getElementById('nombre')
   var refApellido = document.getElementById('apellido')
   var refEdad = document.getElementById('edad')

   var nombre = refNombre.value
   var apellido = refApellido.value
   var edad = refEdad.value
   
   var empleado = { nombre: nombre, apellido: apellido, edad: edad}
   console.log(empleado)
   empleados.push(empleados)

   refNombre.value = ''
   refApellido.value = ''
   refEdad.value = ''

}

function representarEmpleados(){
    var filasTablas = '<tr> <th>nombre</th> <th>Apellido</th> <th>edad</th> </tr>'
    document.getElementById('Tabla').innerHTML
}






function start(){
    console.warn(document.querySelector('title').innerText)
}








/// zona : ejecucion 
start()











