SQL permite combinar el resultado de dos consultas `SELECT` como si fueran conjuntos, siempre que sean **compatibles** (mismo número de columnas y mismo tipo):

- **`UNION`**: junta las filas de las dos consultas y **elimina duplicados**.
- **`UNION ALL`**: junta las filas sin eliminar duplicados — por eso suele ser más rápido que `UNION`, al ahorrarse el paso de comprobar y quitar filas repetidas.
- **`INTERSECT`**: devuelve solo las filas que aparecen en ambas consultas.
- **`EXCEPT`**: devuelve las filas de la primera consulta que no aparecen en la segunda.

[[B3 - T3 SQL]]
