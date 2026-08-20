Modelo NoSQL en el que cada fila puede tener **columnas diferentes** — está **desnormalizado**. Cada columna lleva su propio **timestamp**, generado por el propio producto. Ejemplos de producto: Cassandra, HBase, Hypertable, Bigtable.

Se organiza en **4 dimensiones**: **Keyspace – Column Family – Rowkey – Column**. Un **Keyspace** (≈ Schema) contiene **Column Families** (≈ Table); cada Column Family tiene *Settings* y filas (**Row**); cada fila tiene una **Row Key** y varias **Columns**; y cada columna guarda un par (Key, Value) más su **Timestamp**.

**Ampliación (conocimiento general, no viene del tema):** "desnormalizado" es lo contrario de lo que persigue el modelo relacional (ver **[[Normalización]]**): en vez de evitar redundancia dividiendo en tablas normalizadas, el modelo de columnas duplica y agrupa deliberadamente los datos que se van a leer juntos, para que una lectura típica no necesite hacer JOIN entre varias tablas — se optimiza para lectura rápida a costa de espacio y de la dificultad de mantener consistentes los datos duplicados.

[[B2 - T5 NOSQL Y BIG DATA]]
