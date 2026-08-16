Un **trigger** (disparador) es lógica de negocio con una o varias sentencias que se ejecuta automáticamente a partir de un evento sobre un objeto (normalmente `INSERT`/`UPDATE`/`DELETE` de una tabla).

Se dispara **antes** (`BEFORE`) o **después** (`AFTER`) del cambio, o en su lugar (`INSTEAD OF`) — este último **anula la sentencia original** y solo tiene efecto el cuerpo del trigger (uso típico: seguridad, o convertir un `DELETE` en un `INSERT` en una tabla de auditoría). También puede ser de fila (`FOR EACH ROW`, una ejecución por registro afectado) o de sentencia (`FOR EACH STATEMENT`, una única ejecución por sentencia).

Para acceder a los valores antes/después del cambio, cada SGBD expone sus propias pseudotablas/pseudorregistros:

| Momento | Oracle | MS SQL Server |
|---|---|---|
| Antes del cambio | Old | Deleted |
| Después del cambio | New | Inserted |

Restricciones: un trigger no acepta parámetros, y no puede usar `START TRANSACTION`/`COMMIT`/`ROLLBACK` — no se puede meter una transacción dentro de un trigger.

Usos típicos más allá de la auditoría: aplicar reglas de negocio complejas que un simple `CHECK` no puede expresar, mantener datos derivados/agregados sincronizados automáticamente, o replicar cambios hacia otra tabla/sistema.

[[B3 - T3 SQL]]
