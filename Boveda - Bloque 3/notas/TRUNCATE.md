**TRUNCATE** es la sentencia que vacía una tabla por completo, de forma mucho más rápida que un `DELETE`:

- Hace un borrado rápido, marcando zonas de memoria de golpe (extents = data pages), en vez de borrar fila a fila.
- **Se salta los controles** que sí respeta `DELETE`.
- Deja intactos nombres de columnas, índices y estructuras — la estructura de la tabla persiste.
- **No usa `WHERE`**: borra siempre todas las filas.
- No deja registros en el fichero de log.
- En muchos SGBD (MySQL, SQL Server) también reinicia los contadores autoincrementales/IDENTITY, algo que `DELETE` no hace.

Su comportamiento exacto varía por fabricante: en **Oracle** hace `COMMIT` automáticamente, así que **no se puede deshacer**; en **MySQL** hace falta el privilegio de **DROP**, porque internamente sí borra la tabla y la vuelve a crear (lo que contrasta con la idea general de que "no se borra la tabla para crearla de nuevo").

Formalmente está definida como sentencia DDL, aunque según el fabricante podría considerarse DML.

[[B3 - T3 SQL]]
