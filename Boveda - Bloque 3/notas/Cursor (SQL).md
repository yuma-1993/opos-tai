Un **cursor** es un objeto que permite recorrer, fila a fila, el resultado de una sentencia `SELECT` dentro de un [[Procedimiento almacenado (Stored Procedure)|procedimiento almacenado]]. Un `DataReader` (.NET) y un `ResultSet` (JDBC) son, por debajo, cursores.

```sql
var_reg cursor_tabla%ROWTYPE; -- define la variable con la estructura del cursor cursor_tabla
...
FETCH cursor_tabla INTO var_reg;
...
```

Los cursores procesan fila a fila, lo contrario del enfoque "por conjuntos" (*set-based*) que es natural en SQL — por eso suelen ser más lentos que una sentencia SQL equivalente que opere sobre todo el conjunto de filas a la vez. Se usan cuando la lógica realmente necesita tratar cada fila de forma distinta, algo que no siempre se puede expresar en una sola sentencia declarativa.

[[B3 - T3 SQL]]
