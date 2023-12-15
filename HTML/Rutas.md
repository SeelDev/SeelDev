# Rutas
donde se encuentran los ``recursos ``
### Relativas: 
indica como llegar espeficiamente al archivo que estemos por usar 
como salir de las carpetas : ``../``
### Absolutas:
camino completo hacia el recurso; perfecto para utilizarlos en recursos externos que se encuentra afuerda de nuestro codigo
ejemplo:

`` https://campus-ademass.com/curso/1`` ; es una ruta absoluta 
<hr> 


### Enlaces
base de la estructura web, sale de la pagina que estemos viendo para mostrar el contenido del enlace en otra pagina
 `` <a href="documento2.html" target="_top">Mira el doc 2</a>``
 
``a``: ancla; define enlaces

atributo; ``href`` : complementa el ancla; indica la ruta pa poder llegar al doc que enlazamos

Para hacer un enlace de ruta relativa, primero;

``a href: "documento/documento2"``

el ``documento/``: es la carpeta donde esta guardado el documento2, por lo tanto es necesario indicar donde se encuentra el Documento2

### target
codifica como va a ser el comportamiento de nuestro archivo enlazado a la hora de abrirse, donde queremos abrirlo

``self y parent``; se abre en la misma pestaña del enlace

``blank``; abrir en una pestaña diferente ejemplo un pdf

``top``: abrir el enlace en el body de la pag
<hr>

# imagenes

``<img src="" alt="">``

``atributo src``: carga la imagen que queremos visualizar

``alt``: explica que significa la imagen o que se muestra (no se muestra en la pagina)

### tamaño de img
``width="" ``; anchura
``height=""``; altura 
<hr>

# videos
`` <video src=""></video>``

  ``<video src="videos/2023-11-24 19-52-05.mkv"></video>``  ejemplo
podemos agregarles tamaños

formato; podemos ``especificar las rutas``
.mp4

.ogg

.webm

### controles para manejar el video:

<video ``controls``

``autoplay``: el video se empieza a reproducir apenas entremos a la pag

``loop``: empieza de nuevo el video cuando termina
<hr>

# audio
``<audio src="audio/WhatsApp Audio 2023-12-12 at 14.20.02.ogg"></audio>``

formatos: especificar la ruta 

.mp3

.wav

``iframe`` etiqueta
incrustra html adentro de otra en una seccion determinada
se pueden poner tamaños
