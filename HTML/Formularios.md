# FORMULARIOS
los usuarios se comunican e interactuan con la pagina y con los programadores

ejemplo; caja de comentarios
``<form action=""></form>``

### action
ruta que procesa los datos (donde se envian los datos de los usuarios)
### method
como viajan los datos para procesar (VERBOS: get put post option )
### verbos
``get``: datos no privados
``post``: datos privados (encripta la info) form de loging

 `` <form method="post"
    action="backend/form.php">
    </form>``

~~que envia???

~~cajas de texto: INPUTS DE TEXTO 

``label``: texto explicativo de lo que tiene que insertar el usuario

``SELECT``: seleccionar la opcion que necesite de las que esten disponibles

### Radio
    ``<input type="radio" name="comida" value="arroz" id="arroz"> <label for="arroz">Arroz</label>``
    
   `` <input type="radio" name="comida" value="pollo" id="pollo"> <label for="pollo">Pollo</label>``

### checkbox, seleccion multiple

    <input type="checkbox" name="Terminos" value="yes"> <label for="terminos">Acepto terminos y condiciones</label>

### Rango
    <input type="range" name="Porcentaje" min="0" max="100">
    
### Textarea 

``<form method="post" action="backend/form.php">
     <textarea name="comentario" id="" cols="30" rows="10" placeholder="Escribe aqui tu comentario..." required></textarea> 
        <input type="submit" value="Enviar">``
  
   
<!--Validaciones required-->

<!--Envios-->
<hr>

# estructura de la pag
darle un orden a la pagina
etiquetas; organizan el contenido dentro de la pagina para que esta sea mas leible;
 `` <header>`` <!--Cabezera; menu de navegacion de pagina-->
  ``  </header>``
   `` <main>`` <!--Principal; contenido principal de una pagina-->
  ``  </main>``
    ``<footer>`` <!--Pie; contenido enlaces de refuerzo y legales-->
   `` </footer>``

### Navegacion; menu para navegar en el sitio web 
``<nav></nav>``

una lista no ordenada ``ul>li*n ``

El navegador- lista no ordenada (ul)- enlaces para redireccionar a la pagina correspondiente

`` main``: seccion de contenido principal
 ``<section>`` <!-- divide las secciones de nuestra pagina principal-->
`` <article>`` <!-- encierra el contenido de un articulo -->
`` <aside> ``<!-- contenido menos importante de la pagina-->
`` <nav>`` <!--navegador del sitio web (menu)-->
