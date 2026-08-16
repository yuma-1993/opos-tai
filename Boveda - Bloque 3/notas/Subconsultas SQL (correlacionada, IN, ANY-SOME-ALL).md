Una **subconsulta** es una sentencia `SELECT` anidada dentro de otra (normalmente en su `WHERE`). Hay tres formas principales de usarla:

- **Subconsulta correlacionada** (`WHERE EXISTS (subquery)`): hace referencia a columnas de la consulta externa/principal, así que se re-evalúa por cada fila de esa consulta externa. Devuelve `true` si la subquery devuelve alguna fila. Ejemplo: `SELECT nombre FROM Autor a WHERE EXISTS (SELECT 1 FROM Libro l WHERE l.id_autor = a.id)` → devuelve los autores que tienen al menos un libro.
- **`IN` / `NOT IN`** (`WHERE col1 [NOT] IN (SELECT col2 FROM ...)`): operador de conjuntos — comprueba si el valor de la columna está (o no) en el conjunto de resultados de la subconsulta.
- **`ANY`/`SOME`/`ALL`** (`WHERE col1 <operador> ANY/SOME (SELECT col2 FROM ...)` o con `ALL`): compara el valor con cada fila devuelta por la subconsulta usando un operador (`=`, `>=`...) o una función de agregado; con `ANY`/`SOME` basta con que se cumpla para una fila, con `ALL` tiene que cumplirse para todas.

[[B3 - T3 SQL]]
