Los **niveles de aislamiento** (se configuran con `SET TRANSACTION`) regulan cuánto se protege una transacción de ver cambios hechos por otras transacciones concurrentes. De menos a más estricto:

| Isolation Level | Lectura sucia | Lectura no repetible | Lectura fantasma |
|---|---|---|---|
| READ UNCOMMITTED | SI | SI | SI |
| READ COMMITTED | NO | SI | SI |
| REPEATABLE READ | NO | NO | SI |
| SERIALIZABLE | NO | NO | NO |

- **READ UNCOMMITTED**: se pueden leer datos no consolidados (no confirmados) de otras transacciones.
- **READ COMMITTED**: es el nivel usado por defecto en la mayoría de SGBD.
- **REPEATABLE READ**: si tx1 consulta y tx2 cambia y hace commit, tx1 no verá los nuevos datos de tx2 hasta que termine su propia transacción — desde que tx1 empieza, trabaja siempre con los mismos datos.
- **SERIALIZABLE**: pone las transacciones en fila, una detrás de otra. 0% problemas de concurrencia, pero ↓ rendimiento.

Las tres **lecturas anómalas** que estos niveles evitan (o permiten):
- **Lectura sucia** (*dirty read*): leer datos aún no confirmados de otra transacción, que podría hacer rollback después.
- **Lectura no repetible**: si tx1 es larga, tx2 puede alterar los datos que usaba tx1; si tx1 vuelve a leer, los datos habrán cambiado.
- **Lectura fantasma** (*phantom read*): no se bloquean rangos/grupos de datos, solo filas concretas — tx1 puede recuperar un rango 1-5 y tx2 insertar un registro con valor 3; tx1 no vería ese valor 3 al releer.

> [!important]
> Se pueden bloquear filas o columnas, pero **el bloqueo de tabla completa solo se consigue con SERIALIZABLE**.

> [!note] Ampliación (conocimiento general)
> Muchos SGBD modernos (PostgreSQL, MySQL/InnoDB) no implementan estos niveles solo con bloqueos, sino con **MVCC** (Multi-Version Concurrency Control): cada transacción ve una "foto" consistente de los datos en un instante dado, sin necesidad de bloquear tanto. El trade-off rendimiento/seguridad entre niveles se mantiene igual aunque el mecanismo interno cambie.

Estos niveles existen para proteger la propiedad de **Aislamiento** de [[ACID (transacciones)|ACID]].

[[B3 - T3 SQL]]

Frente al modelo [[BASE (Basically Available, Soft State, Eventually Consistent)|BASE]] (consistencia eventual) de las bases de datos NoSQL: [[B2 - T5 NOSQL Y BIG DATA]].
