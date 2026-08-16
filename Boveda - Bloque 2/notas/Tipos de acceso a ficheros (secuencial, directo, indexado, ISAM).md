Hay cuatro formas clásicas de acceder a los registros de un fichero:

- **Secuencial**: se busca desde el inicio (ejemplo típico: cinta). El borrado es **lógico**, porque no puede hacerse físicamente, y los registros nuevos se añaden al final.
- **Directo**: una clave del registro, o una función sobre esa clave, posiciona directamente en el fichero.
- **Indexado**: hay un fichero para el **índice** y otro para los **datos**; se busca la clave en el índice y este da la posición en el fichero de datos. Es el más novedoso de los tres.
- **Híbrido o ISAM**: combina acceso **indexado** para el índice y **secuencial** para los datos (ejemplo: MyISAM de MySQL).

El índice de un acceso indexado o ISAM se implementa típicamente con un **[[Árbol B, B+ y B-estrella|árbol B o B+]]**, que están pensados justo para minimizar lecturas de disco.

[[B2 - T3 ESTRUCTURAS DE DATOS Y ALGORITMOS]]
[[B3 - T3 SQL]]
