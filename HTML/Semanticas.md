# listas
1) ordenadas:``<ol> </ol> ``(lista enumerada)
2) no ordenadas:`` <ul> </ul>`` (lista punteada)


### elementos de la lista;
etiqueta ``<li> </li>`` (dependientemente de si es ordenada o no, se usa la misma igual)

### emmet de listas;
~~ abreviacion emmet: 
formula:`` <!--tipo-de-la-lista>li*numero-de-elementos-->``
<hr>

# Tablas:
~~ etiqueta de apertura 
<table>
<tr> <!--filas-->
            <td>Celda 1</td> <!-- celdas-->
            <td>Celda 2</td>
            <td>Celda 3</td>
            <td>Celda 4</td>
            <td>Celda 5</td>
    </tr>
</table>

una linea con 5 celdas seguidas y otra linea con 5 celdas seguidas

``th``-> tabla de encabezado (resalta)

<br>

# Semantica:
~~ titulo: ``<caption>Mi primera tabla</caption> ``

~~ atributos de celda:  ``<td colspan="2">`` (se expande 2 celdas a la derecha mas ademas de la que ya esta definida)
``<td rowspan="2">Celda</td> ``(se expande 2 celdas a  abajo ademas de la que ya esta definida)

css: borde a las celdas

### definiciones (divisiones de tablas);
``<thead>``
    cabeza de la tabla
``</thead>``

``<tbody>``
    cuerpo de la tabla
``</tbody>``

``<tfoot>``
    pie de la linea
``</tfoot>``
