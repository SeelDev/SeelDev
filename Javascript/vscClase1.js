<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clase 1- Javascript desde 0</title>
    <style>
    h1 {
        color: slateblue;
    }
    </style>
</head>
<body>
    <h1>Bienvenidos al curso de Javascript!!!</h1>

    <script>
       /*  Uso del console.log
        (sirve para enviar mensajes a la consola)
        esto es un comentario en bloque */
        //shit+alt+a
      
        console.log("hola mundo"); // mensaje inicial de linea
        console.log('como estan?');
       
      //  console.log(1,2,3,4,5) // comentario de linea
      
        /* ---------------------
        
        contenedor dinamico de info
        1) declarar variable
        2) asigno un valor

        ------------------------- */
//lowerCamelCase
    var miMensaje = 'Hola soy un programa en JS'
        console.log(miMensaje)
        /* document.write(miMensaje) //en el body
        alert(miMensaje) //funcion del navegador notificacion */

        var modo = 'info'
        console.log(modo)
//se puede reasignar un valor
        modo ='warning'
        console.warn(modo)

        modo = 'error'
        console.error(modo)


       /*  tipos de variables en js */
       //varisble del tipo number
        var miNumero= -123.45
        console.log(miNumero, typeof miNumero) //que tipo de cont tiene

          //varisble del tipo string
          var miString= 'hola'
        console.log(miString, typeof miString)

          //varisble del tipo booleana
          var miBooleana= false //true
        console.log(miBooleana, typeof miBooleana)

        //si no asignamos valor

         //varisble del tipo indefinida
         var indefinida
        console.log(indefinida, typeof indefinida)

         //varisble del tipo null
         var nula = null
        console.log(nula, typeof nula)

        // variable del tipo array (object)
        // indice -- 0 1 2 3 4 (nombre)
        var miArray = [1,2,3,4]
        console.log(miArray, typeof miArray, Array.isArray(miArray)) //type object
        //Array.isArray(miArray) booleano si es o no array

         // variable del tipo object
        // key/value o clave/valor
        //var miObjeto = {n1:1,n2:2}  //n1= nombre
        var miObjeto = {0:1,1:2}  //0,1= nombre
        console.log(miObjeto, typeof miObjeto, Array.isArray(miArray)) 

        /* tipado en JS (dinamico / debil) */
        var nombreDeUnaPersona= 'Pedro'         //tipado dinamico
        console.log(nombreDeUnaPersona, typeof nombreDeUnaPersona)
        nombreDeUnaPersona= 'Ana'           //tipado debil   
        console.log(nombreDeUnaPersona, typeof nombreDeUnaPersona)


        /* OPERACIONES ARITMETICAS EN JS */

        var numero = (3.5 + 4 - 2) * 5 / 2
        console.log(numero)
        //resultado en console

        var numero2= 5
        numero= 45 + numero2
        console.log(numero)


        var nombre= 'Caro'
        console.log(nombre)


        var numero= 67 + 100
        console.log(numero)



        var mensaje= 'Holita'
        document.write(mensaje)
    </script>

    


</body>
</html>
