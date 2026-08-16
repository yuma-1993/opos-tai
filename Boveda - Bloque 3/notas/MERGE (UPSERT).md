**MERGE** fusiona una tabla origen (**source**) sobre una tabla destino (**target**) en base a una condición de búsqueda: si un registro existe en ambas tablas, **actualiza** el destino; si existe solo en el origen, lo **inserta** en el destino.

```sql
MERGE INTO <nom_tabla_target>
USING <nom_tab_source>
ON <condicion_busqueda>
WHEN MATCHED
  THEN UPDATE SET col1 = ...
WHEN NOT MATCHED
  THEN INSERT (col1, ...) VALUES (..., ...)
```

Es la sentencia estándar SQL para lo que en muchos entornos se conoce coloquialmente como **UPSERT** (UPDATE + INSERT).

[[B3 - T3 SQL]]
