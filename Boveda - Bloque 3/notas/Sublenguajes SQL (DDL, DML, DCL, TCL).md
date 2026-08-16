SQL se divide en cuatro sublenguajes según qué tipo de operación realizan:

| Sublenguaje | Nombre completo | Para qué |
|---|---|---|
| **DDL** | Lenguaje de Definición de Datos | Creación / borrado / modificación de **objetos** (`CREATE`/`DROP`/`ALTER` sobre TABLE, INDEX, [[Dominio\|DOMAIN]], PROCEDURE, [[Trigger (disparador) SQL\|TRIGGER]], SCHEMA, ROLE) |
| **DML** | Lenguaje de Manipulación de Datos | Consulta / borrado / modificación / inserción de **datos** (`SELECT`, `UPDATE`, `INSERT`, `DELETE`, [[MERGE (UPSERT)\|MERGE]]) |
| **DCL** | Lenguaje de Control de Datos | Control del **acceso** a los datos (`GRANT`/`REVOKE` de privilegios sobre un objeto a un usuario o rol) |
| **TCL** | Lenguaje de Control de Transacciones | Control de [[ACID (transacciones)\|transacciones]] (`COMMIT`, `ROLLBACK`, `SAVEPOINT`...) |

> [!important]
> TCL suele tratarse como una parte del DCL, no como un sublenguaje totalmente independiente — es una distinción que varía según la fuente.

La [[Reglas de Codd|Regla 5 de Codd]] ("Sublenguaje de datos completo") exige justamente que exista un lenguaje único que cubra definición, manipulación y consulta — SQL es el ejemplo que la propia regla cita.

Sobre las restricciones (`PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `UNIQUE`) que se definen en DDL, ver [[Claves (superclave, candidata, primaria, alternativa)|Claves]] y [[Restricciones de integridad (relacional)]].

[[B3 - T3 SQL]]
