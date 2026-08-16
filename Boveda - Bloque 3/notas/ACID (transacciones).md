**ACID** son las cuatro propiedades que debe garantizar una **transacción** para considerarse fiable: **A**tomicidad, **C**onsistencia, **A**islamiento, **D**urabilidad.

Una **transacción** es un conjunto de sentencias SQL que se ejecutan como un proceso atómico: se hacen todas, o no se hace ninguna.

- **Atomicidad**: sin ella, una transacción puede quedar a medias (ej. se descuenta saldo de una cuenta pero no se abona en la otra).
- **Consistencia**: la base de datos pasa de un estado válido a otro estado válido, respetando sus reglas de integridad.
- **Aislamiento**: dos transacciones concurrentes no deben interferir entre sí viendo datos intermedios inconsistentes — de ahí las lecturas anómalas (sucia, no repetible, fantasma) que definen los [[Niveles de aislamiento y lecturas anómalas (SQL)|niveles de aislamiento]].
- **Durabilidad**: una vez confirmada (COMMIT), la transacción sobrevive a un fallo posterior del sistema.

[[B3 - T3 SQL]]
