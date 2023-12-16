# CSS

## cascadas de estilos

### como usar css en html 


<!-- EJEMPLO: codigo en css en una hoja HTML; ya no hay atributos es puramente lenguaje css-->
     <style> 
        h1 {
            color: blueviolet;
        }
    </style>
 <!--EJEMPLO: INLINE usa style como ARGUMENTO para darle el diseño a la etiqueta h2-->
    <h2 style="color: darkblue;"> Vaquita bello</h2>

 <!-- vincula css con html-->
    <link rel="stylesheet" href="style.css">

<hr>

# sintaxis
secuencia de instrucciones de estilo siguendo a la siguiente sintaxis


1) ``selector ``: elemento el cual se va a rellenar con un conjunto de reglas entre llaves 
pueden ser: una etiqueta; nombre de una clase; id de un elemento

ejemplo:


``h1 {``

   `` color: brown;``
   
``}``

/ siendo ``h1`` el  ``selector`` /

/ ``color`` la regla (``propiedad``) /

/ brown el ``valor``; (define el valor de la propiedad) /


``p {``

    color: darkmagenta;
    
    font-size: 14px;
    
``}``



### selectores

~~tipos

``etiqueta``; para todas las etiquetas``h1`` ``h2`` ``h3`` ``h4`` ``p`` (mas amplio; implica a todos los elementos de forma general)
p {
    color: darkmagenta;
    font-size: 14px;
}


``de clases`` ; de ``forma individual``, aplicar el estilo a unos pocos h1 h2 p etc.
// conjunto de reglas: para hacer un conjunto de clases; dentro de la etiqueta ``<p class="example">dmWOICWDN</p>``

// se coloca un ``class="nombreDeClase"`` y para que este se vea reflejado en la hoja de style.css; ``.nombreDeClase``;

// siendo ``.`` el que especifica que se trata de una clase de etiqueta que quiere tener un color diferente a los demas; por ejemplo cuando un parrafo tiene distintos argumentos y es necesario remarcarlos con diferentes colores

``identificadores`` ; mas concreto; ``id="nombreUnico"``, a las etiquetas para identificarlas se le pone un ``id`` el cual debe contener un ``nombre UNICO`` para cada etiqueta

para insertarlo en nuestra hoja de estilos; ``#nombreUnico``;

siendo ``#`` el que identidica que se trata sobre un id 

``#myP {``

    ``color: chartreuse;``
    
   `` font-size: 100px;``
   
``}``

<hr>

# Particularidades
``agrupacion de contenidos`` ; en vez de copiar y pegar se puede:

``h1, h2, h3, h4, h5, h6 .title, #myTitle {``

    color: brown;
   
   ``font-size: 70px;``
   
``}``

agrupando las etiquetas h1 - h6 si las caracteristicas de estilos se complementan; si tenemos una etiqueta que individualmente tiene mas caracteristicas 

``h1 {``

    margin: 40px;
    
``}``

``anidamiento`` (anidar)
dentro de una etiqueta tenemos un contenido el cual queremos darle un estilo, por ejemplo, si hay dos 
`` <a href="#">miraaa</a>``  ``<a href="#">lee mas </a>`` pero uno esta adentro de una etiqueta like 

``<div class="card">``
    
        <h3>lindo</h3>
    
       <a href="#">lee mas</a>
 
   `` </div>``
   
se puede ``anidar`` en la hoja de estilos de esta manera

``.card a {``

    color: aqua;
    
``}``

sabiendo que la ``class`` de este div es ``card``, podemos entender es una ``agrupacion de clases``;
``a`` lo que queremos que tenga el estilo

``selector de atributo ``

``a[href="/"] {``

    color: darksalmon;
    
``}``

<hr>

### while card
todo lo que no tiene un color especifico se puede agrupar en una while card para darles el mismo color a todos

### jerarquia
mas concreto, mejor es

``!important`` ; el elemento tiene un ``valor mayor`` en la jerarquia de titulos y todos los demas ``se pintan del mismo color`` 

ejemplo

``h1{``

    color: yellow !important;
    
``}``

ejemplo

``.title{``

    color: violet;

``}``

``#titleId`` {

    color: tomato;
    
``}``

``!important``; aunque hayan colores ya definidos, se ``pisan`` y se pintan del color mas importante
<hr>

### pseudo selectores
aplica distintos estilos en funcion del ``estado de un elemento``
``:hover`` ; hace que el color del "ejemplo ``button`` " cambie cuando el puntero del mouse pase por arriba 

``button:hover {``

    background-color: yellow;
    
``}``

``:focus`` ; al apretar el boton, el color del mismo ``cambia``

``button:focus {``

    background-color: tomato;
    
``}``
