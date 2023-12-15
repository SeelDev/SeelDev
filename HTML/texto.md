###TEXTOS EN HTML:
~~ titulos: (tipo de etiqueta; comportamiento de bloque, no tiene contenido al lado, salta al siguiente bloque de codigo)
titulos con etiquetas del <h1> </h1> al <h6> </h6> (sin necesidad de ningun atributo)
h: contenido destacado en nuestros textos
numero (1-6): indica la importancia que tiene el contenido en nuestro texto; el h1 es el mas importante y h6 el menos importante h1>h6
tienen ``valor semantico``; no hay que usar muchas veces el h1 

~~ parrafos:`` siguen una misma linea de codigo``, no limpian lo que tienen a su alrededor (tipo de etiiqueta: en linea por defecto)
  <p> parrafo </p>
  
  <i>cursiva</i>

  <b>negrita</b>

  <strong>negrita(plus)</strong>

  <del>Tachado</del>

  <u>Subrayado</u>

  <sub>subindices</sub>

  <sup>superindices</sup>

  <small>textos pequeños</small>

~~aux
<br> <!-- salto de linea -->

<hr> <!--dibuja una linea dedivision horizontal-->

~~ ejemplo: 
 <h1>Titulo 1</h1>
  <p>Hola soy un parrafo con cantidad de efectos. Por ejemplo, <i>esta frase está en cursiva, </i> mientras que <strong>aquí estamos escribiendo en negrita de diferentes formas.</strong>Forcemos ahora un salto de linea. <br>
Escribamoos <del>texto tachado</del> o mejor aun, <u>subrayado</u></p>
<br>
<p>En este nuevo parrado, probemos a escrbir <small>un texto pequeño</small>. Tambien podemos ver como resultan los <sub>subindices</sub> y los <sup>superindices</sup></p>
<br>
<p>Por ultimo, terminemos dibujando una linea de division horizontal:</p>
<br>
<hr>
