`EXPLAIN PLAN` es la sentencia que muestra el **plan de ejecución** que va a seguir el SGBD para resolver una consulta (`SELECT`, `INSERT`, `UPDATE` o `DELETE`): la secuencia de operaciones internas (qué índices usa, en qué orden accede a las tablas...) que el motor va a realizar.

La sintaxis varía por fabricante: MySQL y PostgreSQL usan `EXPLAIN <sentencia>` directamente; Oracle usa `EXPLAIN PLAN FOR <sentencia>` y después consulta el resultado con `DBMS_XPLAN`.

[[B3 - T3 SQL]]
